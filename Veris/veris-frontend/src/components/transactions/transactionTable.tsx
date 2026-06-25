import type { Transaction } from "../../types/transaction";

interface Props {
  transactions: Transaction[];
}

export default function TransactionTable({
  transactions,
}: Props) {
  
  console.log(
    "transactionTable received:",
    transactions
  );
  
  return (
    <div className="bg-white rounded-lg shadow overflow-hidden">
      <table className="w-full">
        <thead className="bg-gray-100">
          <tr>
            <th className="p-3 text-left">Transaction ID</th>
            <th className="p-3 text-left">Customer</th>
            <th className="p-3 text-left">Amount</th>
            <th className="p-3 text-left">Fraud</th>
            <th className="p-3 text-left">Credit</th>
            <th className="p-3 text-left">URS</th>
            <th className="p-3 text-left">Risk</th>
            <th className="p-3 text-left">Decision</th>
          </tr>
        </thead>

        <tbody>
          {(transactions ?? []).map((txn) => (
            <tr
              key={txn.id}
              className="border-t"
            >
              <td className="p-3">
                {txn.transaction_id}
              </td>

              <td className="p-3">
                {txn.customer_id}
              </td>

              <td className="p-3">
                ₹{txn.transaction_amount}
              </td>

              <td className="p-3">
                {txn.fraud_score.toFixed(4)}
              </td>

              <td className="p-3">
                {txn.credit_score.toFixed(2)}
              </td>

              <td className="p-3">
                {txn.unified_risk_score.toFixed(4)}
              </td>

              <td className="p-3">
                {txn.risk_tier}
              </td>

              <td className="p-3">
                {txn.decision}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}