export interface Transaction {
  id: number;
  transaction_id: string;
  customer_id: string;
  transaction_amount: number;
  fraud_score: number;
  credit_score: number;
  unified_risk_score: number;
  risk_tier: string;
  decision: string;
  review_status: string;
}