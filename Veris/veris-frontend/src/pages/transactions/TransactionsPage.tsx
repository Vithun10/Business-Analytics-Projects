import { useEffect, useState } from "react";

import TransactionTable from "../../components/transactions/transactionTable";
import { getTransactions } from "../../services/transactionService";
import type { Transaction } from "../../types/transaction";

export default function TransactionsPage() {
  const [transactions, setTransactions] = useState<Transaction[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const loadTransactions = async () => {
      try {
        const data = await getTransactions();

        console.log("API RESPONSE:", data);

        if (Array.isArray(data)) {
          setTransactions(data);
        } else if (data?.transactions) {
          setTransactions(data.transactions);
        } else {
          setTransactions([]);
        }
      } catch (error) {
        console.error("Transactions Error:", error);
        setTransactions([]);
      } finally {
        setLoading(false);
      }
    };

    loadTransactions();
  }, []);

  if (loading) {
    return (
      <div className="text-lg">
        Loading Transactions...
      </div>
    );
  }

  return (
    <div className="space-y-6">
      <h1 className="text-4xl font-bold">
        Transactions
      </h1>

      <TransactionTable
        transactions={transactions}
      />
    </div>
  );
}