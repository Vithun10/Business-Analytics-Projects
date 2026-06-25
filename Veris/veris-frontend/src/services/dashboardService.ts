import { api } from "../api/client";

export const dashboardService = {

  async getOverview() {
    const response = await api.get(
      "/dashboard/overview"
    );

    return response.data;
  },

  async getRiskDistribution() {
    const response = await api.get(
      "/dashboard/risk-distribution"
    );

    return response.data;
  },

  async getDecisionDistribution() {
    const response = await api.get(
      "/dashboard/decision-distribution"
    );

    return response.data;
  },

  async getFraudMetrics() {
    const response = await api.get(
      "/dashboard/fraud-metrics"
    );

    return response.data;
  },

  async getCreditMetrics() {
    const response = await api.get(
      "/dashboard/credit-metrics"
    );

    return response.data;
  },
};

export const getRiskDistribution = async () => {
  const response = await api.get("/dashboard/risk-distribution");
  return response.data;
};

export const getDecisionDistribution = async () => {
  const response = await api.get("/dashboard/decision-distribution");
  return response.data;
};

export const getFraudMetrics = async () => {
  const response = await api.get("/dashboard/fraud-metrics");
  return response.data;
};

export const getCreditMetrics = async () => {
  const response = await api.get("/dashboard/credit-metrics");
  return response.data;
};