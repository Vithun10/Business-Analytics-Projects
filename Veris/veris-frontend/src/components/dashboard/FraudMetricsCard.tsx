interface Props {
  data: {
    average: number;
    maximum: number;
    minimum: number;
  };
}

const FraudMetricsCard = ({ data }: Props) => {
  return (
    <div className="bg-white rounded-lg shadow p-6">
      <h3 className="font-semibold mb-4">
        Fraud Metrics
      </h3>

      <p>Average: {data.average}</p>
      <p>Maximum: {data.maximum}</p>
      <p>Minimum: {data.minimum}</p>
    </div>
  );
};

export default FraudMetricsCard;