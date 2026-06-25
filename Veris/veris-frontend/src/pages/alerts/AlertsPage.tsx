import { useEffect, useState } from "react";
import axios from "axios";

export default function AlertsPage() {
  const [alerts, setAlerts] = useState<any[]>([]);

  useEffect(() => {
    loadAlerts();
  }, []);

  const loadAlerts = async () => {
    try {
      const response = await axios.get(
        "http://127.0.0.1:8000/api/v1/alerts"
      );

      setAlerts(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="space-y-6">
      <h1 className="text-5xl font-bold">
        Alerts Center
      </h1>

      {alerts.length === 0 ? (
        <div className="bg-white rounded-xl shadow p-6">
          No Active Alerts
        </div>
      ) : (
        alerts.map((alert, index) => (
          <div
            key={index}
            className="bg-white rounded-xl shadow p-6"
          >
            <h2 className="text-xl font-semibold">
              {alert.alert_type}
            </h2>

            <p className="mt-2">
              {alert.message}
            </p>

            <p className="text-sm text-gray-500 mt-4">
              {alert.created_at}
            </p>
          </div>
        ))
      )}
    </div>
  );
}