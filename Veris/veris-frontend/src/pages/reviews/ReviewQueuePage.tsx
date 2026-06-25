import { useEffect, useState } from "react";
import axios from "axios";

interface Transaction {
  transaction_id: string;
  customer_id: string;
  transaction_amount: number;
  fraud_score: number;
  credit_score: number;
  unified_risk_score: number;
  risk_tier: string;
  decision: string;
  review_status: string;
}

export default function ReviewQueuePage() {
  const [transactions, setTransactions] = useState<Transaction[]>([]);
  const [loading, setLoading] = useState(true);

  const loadTransactions = async () => {
    try {
      const response = await axios.get(
        "http://127.0.0.1:8000/api/v1/transactions"
      );

      setTransactions(response.data);
    } catch (error) {
      console.error("Failed to load transactions", error);
    } finally {
      setLoading(false);
    }
  };

  const reviewTransaction = async (transactionId: string) => {
    try {
      await axios.patch(
        `http://127.0.0.1:8000/api/v1/decisions/${transactionId}/review?reviewer=manager`
      );

      loadTransactions();
    } catch (error) {
      console.error("Review failed", error);
    }
  };

  useEffect(() => {
    loadTransactions();
  }, []);

  if (loading) {
    return <div>Loading Review Queue...</div>;
  }

  return (
    <div>
      <h1 className="text-4xl font-bold mb-6">
        Review Queue
      </h1>

      <div className="bg-white rounded-xl shadow overflow-hidden">
        <table className="w-full">
          <thead className="border-b">
            <tr className="text-left">
              <th className="p-4">Transaction</th>
              <th className="p-4">Risk Tier</th>
              <th className="p-4">Decision</th>
              <th className="p-4">Review Status</th>
              <th className="p-4">Action</th>
            </tr>
          </thead>

          <tbody>
            {transactions.map((txn) => (
              <tr
                key={txn.transaction_id}
                className="border-b"
              >
                <td className="p-4">
                  {txn.transaction_id}
                </td>

                <td className="p-4">
                  {txn.risk_tier}
                </td>

                <td className="p-4">
                  {txn.decision}
                </td>

                <td className="p-4">
                  {txn.review_status}
                </td>

                <td className="p-4">
                  <button
                    onClick={() =>
                      reviewTransaction(
                        txn.transaction_id
                      )
                    }
                    className="bg-blue-600 text-white px-3 py-1 rounded"
                  >
                    Review
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}