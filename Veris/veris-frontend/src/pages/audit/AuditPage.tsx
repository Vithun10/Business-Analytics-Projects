import { useEffect, useState } from "react";
import axios from "axios";

export default function AuditPage() {
  const [logs, setLogs] = useState<any[]>([]);

  useEffect(() => {
    loadLogs();
  }, []);

  const loadLogs = async () => {
    try {
      const response = await axios.get(
        "http://127.0.0.1:8000/api/v1/audit-log"
      );

      setLogs(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="space-y-6">
      <h1 className="text-5xl font-bold">
        Audit Trail
      </h1>

      <div className="bg-white rounded-xl shadow overflow-hidden">
        <table className="w-full">
          <thead className="border-b bg-gray-50">
            <tr>
              <th className="p-4 text-left">
                Timestamp
              </th>

              <th className="p-4 text-left">
                Action
              </th>

              <th className="p-4 text-left">
                Reviewer
              </th>

              <th className="p-4 text-left">
                Transaction
              </th>
            </tr>
          </thead>

          <tbody>
            {logs.map((log, index) => (
              <tr
                key={index}
                className="border-b"
              >
                <td className="p-4">
                  {log.timestamp}
                </td>

                <td className="p-4">
                  {log.action}
                </td>

                <td className="p-4">
                  {log.reviewer}
                </td>

                <td className="p-4">
                  {log.transaction_id}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}