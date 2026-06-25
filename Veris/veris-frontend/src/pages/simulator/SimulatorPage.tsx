import { useState } from "react";
import axios from "axios";

export default function SimulatorPage() {
  const [fraudScore, setFraudScore] = useState("");
  const [creditRisk, setCreditRisk] = useState("");

  const [result, setResult] = useState<any>(null);

  const runSimulation = async () => {
    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/api/v1/simulator",
        {
          fraud_score: Number(fraudScore),
          credit_risk: Number(creditRisk),
        }
      );

      setResult(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="space-y-6">
      <h1 className="text-5xl font-bold">
        Risk Simulator
      </h1>

      <div className="bg-white rounded-xl shadow p-6">
        <h2 className="text-2xl font-semibold mb-6">
          Unified Risk Score Simulator
        </h2>

        <div className="grid grid-cols-2 gap-6">
          <div>
            <label className="block mb-2 font-medium">
              Fraud Score
            </label>

            <input
              type="number"
              step="0.01"
              min="0"
              max="1"
              value={fraudScore}
              onChange={(e) =>
                setFraudScore(e.target.value)
              }
              className="w-full border rounded-lg p-3"
            />
          </div>

          <div>
            <label className="block mb-2 font-medium">
              Credit Risk
            </label>

            <input
              type="number"
              step="0.01"
              min="0"
              max="1"
              value={creditRisk}
              onChange={(e) =>
                setCreditRisk(e.target.value)
              }
              className="w-full border rounded-lg p-3"
            />
          </div>
        </div>

        <button
          onClick={runSimulation}
          className="mt-6 bg-blue-600 text-white px-6 py-3 rounded-lg"
        >
          Simulate
        </button>
      </div>

      {result && (
        <div className="bg-white rounded-xl shadow p-6">
          <h2 className="text-2xl font-semibold mb-6">
            Simulation Result
          </h2>

          <div className="grid grid-cols-3 gap-6">

            <div>
              <p className="text-gray-500">
                Unified Risk Score
              </p>

              <p className="text-3xl font-bold">
                {result.unified_risk_score}
              </p>
            </div>

            <div>
              <p className="text-gray-500">
                Risk Tier
              </p>

              <p className="text-3xl font-bold">
                {result.risk_tier}
              </p>
            </div>

            <div>
              <p className="text-gray-500">
                Decision
              </p>

              <p className="text-3xl font-bold">
                {result.decision}
              </p>
            </div>

          </div>
        </div>
      )}
    </div>
  );
}