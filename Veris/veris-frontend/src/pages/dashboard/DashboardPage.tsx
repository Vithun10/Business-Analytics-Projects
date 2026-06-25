import { useEffect, useState } from "react";

import MetricCard from "../../components/cards/MetricCard";
import RiskDistributionCard from "../../components/dashboard/RiskDistributionCard";
import DecisionDistributionCard from "../../components/dashboard/DecisionDistributionCard";
import FraudMetricsCard from "../../components/dashboard/FraudMetricsCard";
import CreditMetricsCard from "../../components/dashboard/CreditMetricsCard";

import { dashboardService } from "../../services/dashboardService";

export default function DashboardPage() {
  const [overview, setOverview] = useState<any>(null);

  const [riskDistribution, setRiskDistribution] =
    useState<any>(null);

  const [decisionDistribution, setDecisionDistribution] =
    useState<any>(null);

  const [fraudMetrics, setFraudMetrics] =
    useState<any>(null);

  const [creditMetrics, setCreditMetrics] =
    useState<any>(null);

  useEffect(() => {
    loadDashboard();
  }, []);

  const loadDashboard = async () => {
    try {
      const [
        overview,
        risk,
        decision,
        fraud,
        credit,
      ] = await Promise.all([
        dashboardService.getOverview(),
        dashboardService.getRiskDistribution(),
        dashboardService.getDecisionDistribution(),
        dashboardService.getFraudMetrics(),
        dashboardService.getCreditMetrics(),
      ]);

      setOverview(overview);
      setRiskDistribution(risk);
      setDecisionDistribution(decision);
      setFraudMetrics(fraud);
      setCreditMetrics(credit);

    } catch (error) {
      console.error(
        "Dashboard Load Error",
        error
      );
    }
  };

  if (
    !overview ||
    !riskDistribution ||
    !decisionDistribution ||
    !fraudMetrics ||
    !creditMetrics
  ) {
    return (
      <div className="p-6 text-lg">
        Loading Dashboard...
      </div>
    );
  }

  return (
    <div className="p-6">

      <h1 className="text-5xl font-bold mb-8">
        Dashboard
      </h1>

      {/* KPI CARDS */}

      <div className="grid grid-cols-4 gap-6">

        <MetricCard
          title="Transactions"
          value={overview.total_transactions}
        />

        <MetricCard
          title="Approvals"
          value={overview.approve_count}
        />

        <MetricCard
          title="Reviews"
          value={overview.review_count}
        />

        <MetricCard
          title="Average URS"
          value={overview.average_urs}
        />

      </div>

      {/* ANALYTICS CARDS */}

      <div className="grid grid-cols-2 gap-6 mt-6">

        <RiskDistributionCard
          data={riskDistribution}
        />

        <DecisionDistributionCard
          data={decisionDistribution}
        />

        <FraudMetricsCard
          data={fraudMetrics}
        />

        <CreditMetricsCard
          data={creditMetrics}
        />

      </div>

    </div>
  );
}