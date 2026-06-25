import { useEffect, useState } from "react";
import { getTransactions } from "../../services/transactionService";
import axios from "axios";

export default function AIAnalystPage() {
  const [transactions, setTransactions] = useState<any[]>([]);
  const [selectedTxn, setSelectedTxn] = useState("");
  const [analysis, setAnalysis] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    loadTransactions();
  }, []);

  const loadTransactions = async () => {
  try {
    const data = await getTransactions();

    if (Array.isArray(data)) {
      setTransactions(data);
    } else {
      setTransactions(data.transactions || []);
    }
  } catch (error) {
    console.error(error);
  }
};

  const analyzeTransaction = async () => {
    if (!selectedTxn) return;

    setLoading(true);

    try {
      const response = await axios.get(
        `http://127.0.0.1:8000/api/v1/ai-analyst/${selectedTxn}`
      );

      setAnalysis(response.data);
    } catch (error) {
      console.error(error);
    }

    setLoading(false);
  };

  return (
    <div className="space-y-6">
      <h1 className="text-5xl font-bold">
        AI Analyst
      </h1>

      {/* SELECT TRANSACTION */}

      <div className="bg-white p-6 rounded-xl shadow">
        <h2 className="text-xl font-semibold mb-4">
          Select Transaction
        </h2>

        <div className="flex gap-4">
          <select
            className="border rounded px-4 py-2 w-80"
            value={selectedTxn}
            onChange={(e) =>
              setSelectedTxn(e.target.value)
            }
          >
            <option value="">
              Select Transaction
            </option>

            {transactions.map((txn) => (
              <option
                 key={txn.transaction_id}
                 value={txn.transaction_id}
                 >
                {txn.transaction_id} - {txn.customer_id}
                </option>
            ))}
          </select>

          <button
            onClick={analyzeTransaction}
            className="bg-blue-600 text-white px-5 py-2 rounded"
          >
            Analyze
          </button>
        </div>
      </div>

      {/* RESULT */}

      {loading && (
        <div className="bg-white p-6 rounded-xl shadow">
          Loading Analysis...
        </div>
      )}

      {analysis && (
        <div className="bg-white p-8 rounded-xl shadow">
          <h2 className="text-2xl font-bold mb-6">
            AI Risk Assessment
          </h2>

          <div className="space-y-6">
            <div>
              <p className="text-gray-500">
                Risk Level
              </p>

              <p className="text-2xl font-bold">
                {analysis.risk_level}
              </p>
            </div>

            <div>
              <p className="text-gray-500">
                Decision
              </p>

              <p className="text-2xl font-bold">
                {analysis.decision}
              </p>
            </div>

            <div>
              <p className="text-gray-500">
                AI Summary
              </p>

              <p className="mt-2">
                {analysis.summary}
              </p>
            </div>

            <div>
              <p className="text-gray-500">
                Recommendation
              </p>

              <p className="mt-2">
                {analysis.recommendation}
              </p>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}