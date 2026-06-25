import { Routes, Route } from "react-router-dom";

import AppLayout from "../components/layout/AppLayout";

import DashboardPage from "../pages/dashboard/DashboardPage";
import TransactionsPage from "../pages/transactions/TransactionsPage";
import UploadCenterPage from "../pages/uploads/UploadCenterPage";
import ReviewQueuePage from "../pages/reviews/ReviewQueuePage";
import AnalyticsPage from "../pages/analytics/AnalyticsPage";
import ResearchPage from "../pages/research/ResearchPage";
import ReportsPage from "../pages/reports/ReportsPage";
import SimulatorPage from "../pages/simulator/SimulatorPage";
import AlertsPage from "../pages/alerts/AlertsPage";
import AIAnalystPage from "../pages/ai-analyst/AIAnalystPage";
import AuditPage from "../pages/audit/AuditPage";

export default function AppRoutes() {
  return (
    <Routes>
      <Route element={<AppLayout />}>
        <Route path="/" element={<DashboardPage />} />
        <Route path="/transactions" element={<TransactionsPage />} />
        <Route path="/uploads" element={<UploadCenterPage />} />
        <Route path="/reviews" element={<ReviewQueuePage />} />
        <Route path="/analytics" element={<AnalyticsPage />} />
        <Route path="/research" element={<ResearchPage />} />
        <Route path="/reports" element={<ReportsPage />} />
        <Route path="/simulator" element={<SimulatorPage />} />
        <Route path="/alerts" element={<AlertsPage />} />
        <Route path="/ai-analyst" element={<AIAnalystPage />} />
        <Route path="/audit" element={<AuditPage />} />
      </Route>
    </Routes>
  );
}