import { useEffect, useState } from "react";
import axios from "axios";

export default function ResearchPage() {
  const [overview, setOverview] = useState<any>(null);
  const [models, setModels] = useState<any>(null);

  useEffect(() => {
    loadResearch();
  }, []);

  const loadResearch = async () => {
    try {
      const [overviewRes, modelsRes] = await Promise.all([
        axios.get(
          "http://127.0.0.1:8000/api/v1/research/overview"
        ),
        axios.get(
          "http://127.0.0.1:8000/api/v1/research/models"
        ),
      ]);

      setOverview(overviewRes.data);
      setModels(modelsRes.data);
    } catch (error) {
      console.error(error);
    }
  };

  if (!overview || !models) {
    return (
      <div className="p-6">
        Loading Research Module...
      </div>
    );
  }

  return (
    <div className="space-y-6">
      <h1 className="text-5xl font-bold">
        Research & Methodology
      </h1>

      {/* PLATFORM OVERVIEW */}

      <div className="bg-white rounded-xl shadow p-6">
        <h2 className="text-2xl font-bold mb-4">
          Platform Overview
        </h2>

        <p className="text-gray-700 mb-4">
          {overview.description}
        </p>

        <div className="grid grid-cols-3 gap-4 mt-4">
          {overview.core_modules.map(
            (module: string) => (
              <div
                key={module}
                className="bg-gray-100 rounded-lg p-4"
              >
                {module}
              </div>
            )
          )}
        </div>
      </div>

      {/* FRAUD MODEL */}

      <div className="bg-white rounded-xl shadow p-6">
        <h2 className="text-2xl font-bold mb-4">
          Fraud Detection Model
        </h2>

        <p className="mb-4">
          Ensemble:
          <span className="font-semibold ml-2">
            {models.fraud_model.ensemble}
          </span>
        </p>

        <div className="grid grid-cols-2 gap-6">
          <div>
            <h3 className="font-semibold mb-2">
              Random Forest
            </h3>

            <ul className="space-y-1">
              <li>
                ROC AUC:
                {" "}
                {models.fraud_model.random_forest.roc_auc}
              </li>
              <li>
                Precision:
                {" "}
                {models.fraud_model.random_forest.precision}
              </li>
              <li>
                Recall:
                {" "}
                {models.fraud_model.random_forest.recall}
              </li>
              <li>
                F1:
                {" "}
                {models.fraud_model.random_forest.f1}
              </li>
            </ul>
          </div>

          <div>
            <h3 className="font-semibold mb-2">
              XGBoost
            </h3>

            <ul className="space-y-1">
              <li>
                ROC AUC:
                {" "}
                {models.fraud_model.xgboost.roc_auc}
              </li>
              <li>
                Precision:
                {" "}
                {models.fraud_model.xgboost.precision}
              </li>
              <li>
                Recall:
                {" "}
                {models.fraud_model.xgboost.recall}
              </li>
              <li>
                F1:
                {" "}
                {models.fraud_model.xgboost.f1}
              </li>
            </ul>
          </div>
        </div>
      </div>

      {/* CREDIT MODEL */}

      <div className="bg-white rounded-xl shadow p-6">
        <h2 className="text-2xl font-bold mb-4">
          Proxy Credit Risk Model
        </h2>

        <p className="mb-4">
          Model Type:
          <span className="font-semibold ml-2">
            {models.credit_model.type}
          </span>
        </p>

        <div className="grid grid-cols-2 gap-4">
          {models.credit_model.features.map(
            (feature: string) => (
              <div
                key={feature}
                className="bg-gray-100 rounded-lg p-4"
              >
                {feature}
              </div>
            )
          )}
        </div>
      </div>
    </div>
  );
}