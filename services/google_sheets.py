import gspread
from oauth2client.service_account import ServiceAccountCredentials
from config import SPREADSHEET_ID

def append_to_google_sheet(data):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open_by_key(SPREADSHEET_ID).worksheet("Рекламації")

    row = [
        data.get("fop", ""),
        data.get("phone", ""),
        data.get("factory", ""),
        data.get("product_number", ""),
        data.get("order_number", ""),
        data.get("product_name", ""),
        data.get("reason", ""),
        data.get("part", ""),
        data.get("quantity", "")
    ]
    sheet.append_row(row)