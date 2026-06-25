interface Props {
  data: {
    APPROVE: number;
    REVIEW: number;
    DECLINE: number;
  };
}

const DecisionDistributionCard = ({ data }: Props) => {
  return (
    <div className="bg-white rounded-lg shadow p-6">
      <h3 className="font-semibold mb-4">
        Decision Distribution
      </h3>

      <div className="space-y-2">
        <p>Approve: {data.APPROVE}</p>
        <p>Review: {data.REVIEW}</p>
        <p>Decline: {data.DECLINE}</p>
      </div>
    </div>
  );
};

export default DecisionDistributionCard;