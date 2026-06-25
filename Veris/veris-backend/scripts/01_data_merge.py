import pandas as pd


def merge_datasets():

    transaction_df = pd.read_csv(
        "uploads/train_transaction.csv"
    )

    identity_df = pd.read_csv(
        "uploads/train_identity.csv"
    )

    merged_df = transaction_df.merge(
        identity_df,
        how="left",
        on="TransactionID"
    )

    merged_df.to_csv(
        "processed/merged_transactions.csv",
        index=False
    )

    print(
        f"Merged Shape: {merged_df.shape}"
    )


if __name__ == "__main__":
    merge_datasets()