interface Props {
  data: {
    LOW: number;
    MEDIUM: number;
    HIGH: number;
  };
}

const RiskDistributionCard = ({ data }: Props) => {
  return (
    <div className="bg-white rounded-lg shadow p-6">
      <h3 className="font-semibold mb-4">
        Risk Distribution
      </h3>

      <div className="space-y-2">
        <p>LOW: {data.LOW}</p>
        <p>MEDIUM: {data.MEDIUM}</p>
        <p>HIGH: {data.HIGH}</p>
      </div>
    </div>
  );
};

export default RiskDistributionCard;