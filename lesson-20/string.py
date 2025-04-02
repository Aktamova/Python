import sqlite3
import pandas as pd

conn = sqlite3.connect('chinook.db')

# Load the necessary data from the database
customers = pd.read_sql('SELECT * FROM customers', conn)
invoices = pd.read_sql('SELECT * FROM invoices', conn)

conn.close()

# Merge the customers and invoices tables on the CustomerId column
merged_data = pd.merge(invoices, customers, on='CustomerId', how='inner')

# Calculate the total amount spent by each customer
total_spent = merged_data.groupby(['CustomerId', 'FirstName', 'LastName'])['Total'].sum().reset_index()

# Sort the customers by the total amount spent in descending order
top_5_customers = total_spent.sort_values(by='Total', ascending=False).head(5)

# Display the customer ID, name, and total amount spent for the top 5 customers
top_5_customers[['CustomerId', 'FirstName', 'LastName', 'Total']]

import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('chinook.db')

# Load necessary tables from the database
invoices = pd.read_sql('SELECT * FROM invoices', conn)
invoice_items = pd.read_sql('SELECT * FROM invoice_items', conn)
tracks = pd.read_sql('SELECT * FROM tracks', conn)
albums = pd.read_sql('SELECT * FROM albums', conn)

# Close the database connection
conn.close()

# Merge the invoice_items with tracks to link purchases to albums
invoice_tracks = pd.merge(invoice_items, tracks, on='TrackId', how='inner')

# Merge with albums to get the album info for each track
invoice_tracks = pd.merge(invoice_tracks, albums, on='AlbumId', how='inner')

# Now, we'll group by CustomerId and AlbumId to check if a customer purchased the full album
# A customer is considered to have purchased a full album if they bought all tracks in the album

# Count the number of tracks per album
album_track_counts = invoice_tracks.groupby('AlbumId')['TrackId'].nunique()

# Count the number of tracks purchased by each customer for each album
customer_album_tracks = invoice_tracks.groupby(['CustomerId', 'AlbumId'])['TrackId'].nunique().reset_index()

# Merge the two dataframes to get the total number of tracks in each album
customer_album_tracks = pd.merge(customer_album_tracks, album_track_counts, on='AlbumId', suffixes=('_purchased', '_total'))

# Classify customers as individual tracks or full albums
customer_album_tracks['PurchaseType'] = customer_album_tracks.apply(
    lambda row: 'Full Album' if row['TrackId_purchased'] == row['TrackId_total'] else 'Individual Tracks', axis=1
)

# Now, group by CustomerId and count how many times they fall into each category
purchase_summary = customer_album_tracks.groupby('CustomerId')['PurchaseType'].unique().reset_index()

# A customer prefers "Full Album" if they have only purchased full albums; otherwise, they are categorized as "Individual Tracks"
purchase_summary['CustomerPreference'] = purchase_summary['PurchaseType'].apply(
    lambda x: 'Full Album' if len(x) == 1 and 'Full Album' in x else 'Individual Tracks'
)

# Calculate the percentage of customers in each category
preference_counts = purchase_summary['CustomerPreference'].value_counts(normalize=True) * 100

# Display the percentage summary
print("Percentage of customers who prefer each category:")
print(preference_counts)
