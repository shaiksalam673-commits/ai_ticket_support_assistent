def detect_anomalies(df):

    anomalies = {}

    mean_time = df["resolution_time_hrs"].mean()

    std_time = df["resolution_time_hrs"].std()

    anomalies["long_resolution"] = df[
        df["resolution_time_hrs"]
        >
        mean_time + 2 * std_time
    ]

    anomalies["critical_unresolved"] = df[
        (df["priority"] == "Critical")
        &
        (df["status"] != "Resolved")
    ]

    anomalies["low_ratings"] = df[
        df["customer_rating"] <= 2
    ]

    return anomalies