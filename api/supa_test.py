import hashlib
from supabase import create_client, Client

#supabase data connection: URL, KEY

SUPABASE_URL = "https://rzfodsdhxvkpmhpkmiyr.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJ6Zm9kc2RoeHZrcG1ocGttaXlyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzAxNjY2MzcsImV4cCI6MjA0NTc0MjYzN30.38qSf8BdTJTp2F5XX7N5cBf2it2wH1UH4ta43JpbppA"

#Connet to Supabase Client

supabase: Client = create_client(SUPABASE_URL,SUPABASE_KEY)

#Get data 

def save_data(e, p):
    
    enc_pass = hashlib.sha256(p.encode()).hexdigest()
    response = supabase.table('users').insert({"email": e, "password": enc_pass}).execute()
    
    if response.data:

      print(f"User has been saved successfully: {response.data}")
      
    elif response.error:
        print(f"Error saving user: {response.error}")

#Main
email = input("User e-mail")
password = input("User password")
save_data(email, password)

