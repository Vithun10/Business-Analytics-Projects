import { useEffect, useState } from "react";
import axios from "axios";

import {
  PieChart,
  Pie,
  Cell,
  Tooltip,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  ResponsiveContainer,
} from "recharts";

const COLORS = ["#22c55e", "#f59e0b", "#ef4444"];

export default function AnalyticsPage() {
  const [overview, setOverview] = useState<any>(null);
  const [riskData, setRiskData] = useState<any[]>([]);
  const [decisionData, setDecisionData] = useState<any[]>([]);
  const [fraudMetrics, setFraudMetrics] = useState<any>(null);
  const [creditMetrics, setCreditMetrics] = useState<any>(null);

  const loadAnalytics = async () => {
    try {
      const [
        overviewRes,
        riskRes,
        decisionRes,
        fraudRes,
        creditRes,
      ] = await Promise.all([
        axios.get(
          "http://127.0.0.1:8000/api/v1/dashboard/overview"
        ),
        axios.get(
          "http://127.0.0.1:8000/api/v1/dashboard/risk-distribution"
        ),
        axios.get(
          "http://127.0.0.1:8000/api/v1/dashboard/decision-distribution"
        ),
        axios.get(
          "http://127.0.0.1:8000/api/v1/dashboard/fraud-metrics"
        ),
        axios.get(
          "http://127.0.0.1:8000/api/v1/dashboard/credit-metrics"
        ),
      ]);

      setOverview(overviewRes.data);

      setRiskData([
        {
          name: "LOW",
          value: riskRes.data.LOW || 0,
        },
        {
          name: "MEDIUM",
          value: riskRes.data.MEDIUM || 0,
        },
        {
          name: "HIGH",
          value: riskRes.data.HIGH || 0,
        },
      ]);

      setDecisionData([
        {
          name: "APPROVE",
          value: decisionRes.data.APPROVE || 0,
        },
        {
          name: "REVIEW",
          value: decisionRes.data.REVIEW || 0,
        },
        {
          name: "DECLINE",
          value: decisionRes.data.DECLINE || 0,
        },
      ]);

      setFraudMetrics(fraudRes.data);
      setCreditMetrics(creditRes.data);
    } catch (error) {
      console.error(error);
    }
  };

  useEffect(() => {
    loadAnalytics();
  }, []);

  if (!overview) {
    return (
      <div className="p-6 text-lg">
        Loading Analytics...
      </div>
    );
  }

  return (
    <div className="space-y-6">
      <h1 className="text-5xl font-bold">
        Analytics
      </h1>

      {/* KPI CARDS */}

      <div className="grid grid-cols-4 gap-6">
        <div className="bg-white rounded-xl shadow p-6">
          <p className="text-gray-500">
            Transactions
          </p>
          <h2 className="text-4xl font-bold mt-2">
            {overview.total_transactions}
          </h2>
        </div>

        <div className="bg-white rounded-xl shadow p-6">
          <p className="text-gray-500">
            Approvals
          </p>
          <h2 className="text-4xl font-bold mt-2 text-green-600">
            {overview.approve_count}
          </h2>
        </div>

        <div className="bg-white rounded-xl shadow p-6">
          <p className="text-gray-500">
            Reviews
          </p>
          <h2 className="text-4xl font-bold mt-2 text-yellow-600">
            {overview.review_count}
          </h2>
        </div>

        <div className="bg-white rounded-xl shadow p-6">
          <p className="text-gray-500">
            Average URS
          </p>
          <h2 className="text-4xl font-bold mt-2">
            {overview.average_urs?.toFixed(4)}
          </h2>
        </div>
      </div>

      {/* CHARTS */}

      <div className="grid grid-cols-2 gap-6">
        <div className="bg-white rounded-xl shadow p-6">
          <h2 className="text-xl font-semibold mb-4">
            Risk Distribution
          </h2>

          <ResponsiveContainer
            width="100%"
            height={350}
          >
            <PieChart>
              <Pie
                data={riskData}
                dataKey="value"
                outerRadius={120}
                label
              >
                {riskData.map((_, index) => (
                  <Cell
                    key={index}
                    fill={COLORS[index]}
                  />
                ))}
              </Pie>

              <Tooltip />
            </PieChart>
          </ResponsiveContainer>
        </div>

        <div className="bg-white rounded-xl shadow p-6">
          <h2 className="text-xl font-semibold mb-4">
            Decision Distribution
          </h2>

          <ResponsiveContainer
            width="100%"
            height={350}
          >
            <BarChart data={decisionData}>
              <XAxis dataKey="name" />
              <YAxis />
              <Tooltip />

              <Bar
                dataKey="value"
                fill="#2563eb"
                radius={[8, 8, 0, 0]}
              />
            </BarChart>
          </ResponsiveContainer>
        </div>
      </div>

      {/* METRICS */}

      <div className="grid grid-cols-2 gap-6">
        <div className="bg-white rounded-xl shadow p-6">
          <h2 className="text-xl font-semibold mb-4">
            Fraud Metrics
          </h2>

          <div className="space-y-3 text-lg">
            <p>
              Average Fraud Score:
              <span className="font-semibold ml-2">
                {fraudMetrics.average}
              </span>
            </p>

            <p>
              Maximum:
              <span className="font-semibold ml-2">
                {fraudMetrics.maximum}
              </span>
            </p>

            <p>
              Minimum:
              <span className="font-semibold ml-2">
                {fraudMetrics.minimum}
              </span>
            </p>
          </div>
        </div>

        <div className="bg-white rounded-xl shadow p-6">
          <h2 className="text-xl font-semibold mb-4">
            Credit Metrics
          </h2>

          <div className="space-y-3 text-lg">
            <p>
              Average Credit Score:
              <span className="font-semibold ml-2">
                {creditMetrics.average}
              </span>
            </p>

            <p>
              Maximum:
              <span className="font-semibold ml-2">
                {creditMetrics.maximum}
              </span>
            </p>

            <p>
              Minimum:
              <span className="font-semibold ml-2">
                {creditMetrics.minimum}
              </span>
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}