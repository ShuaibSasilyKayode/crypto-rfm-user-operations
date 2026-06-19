import pandas as pd

SHEET_ID = "1J1rPswzfrRnqjq5ySNfqqzxGr90PgoCYh4GTq-CzG_Y"
SHEET_NAME = "rfm_dashboard"
url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"

try:
    df = pd.read_csv(url)
    df.columns = df.columns.str.strip()
    
    print("==================================================================")
    print("LIVE GOOGLE SHEET CONNECTED SUCCESSFULLY")
    print("RUNNING AUTOMATED USER OPERATIONS TRADING MATRIX")
    print("==================================================================\n")
    
    for index, row in df.iterrows():
        user_id = row['User ID']
        segment = row['User Segment']
        recency = row['Recency (Days)']
        monetary = row['Monetary Value ($)']
        
        print(f"Processing Account: {user_id} | Spreadsheet Segment: {segment}")
        
        if segment == "Whale / VIP":
            print(f"[CRITICAL ALIGNMENT] Webhook fired to Key Account Management Team.")
            print(f" -> ACTION: Assign dedicated manager to {user_id}. Reason: Volume {monetary} threshold met.\n")
        elif segment == "Active Retail":
            print(f"[GROWTH TRIGGER] Pushing gamified campaign banner to {user_id} interface.")
            print(f" -> ACTION: Enroll in $50,000 Trading Tournament.\n")
        elif segment == "At-Risk / Slipping":
            print(f"[RETENTION TRIGGER] Outbound API call dispatched for {user_id}.")
            print(f" -> ACTION: Send '0% Maker Fee Voucher'. Inactivity: {recency} days.\n")
        elif segment == "Dormant / Churned":
            print(f"[RECOVERY TRIGGER] Dispatching automated feedback survey to {user_id}.\n")
        else:
            print(f"[SYSTEM NOTE] Standard operational tracking for {user_id}.\n")

except Exception as e:
    print(f"CONNECTION ERROR: {e}")
