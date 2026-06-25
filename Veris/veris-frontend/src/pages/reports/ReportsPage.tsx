export default function ReportsPage() {
  const downloadJson = () => {
    window.open(
      "http://127.0.0.1:8000/api/v1/reports/export/json",
      "_blank"
    );
  };

  const downloadCsv = () => {
    window.open(
      "http://127.0.0.1:8000/api/v1/reports/export/csv",
      "_blank"
    );
  };

  return (
    <div className="space-y-6">
      <h1 className="text-5xl font-bold">
        Reports Center
      </h1>

      <div className="grid grid-cols-2 gap-6">

        <div className="bg-white p-8 rounded-xl shadow">
          <h2 className="text-2xl font-semibold mb-4">
            Export JSON Report
          </h2>

          <p className="text-gray-600 mb-6">
            Download complete transaction and
            risk assessment data in JSON format.
          </p>

          <button
            onClick={downloadJson}
            className="bg-blue-600 text-white px-6 py-3 rounded-lg"
          >
            Download JSON
          </button>
        </div>

        <div className="bg-white p-8 rounded-xl shadow">
          <h2 className="text-2xl font-semibold mb-4">
            Export CSV Report
          </h2>

          <p className="text-gray-600 mb-6">
            Download transaction records as CSV.
          </p>

          <button
            onClick={downloadCsv}
            className="bg-green-600 text-white px-6 py-3 rounded-lg"
          >
            Download CSV
          </button>
        </div>

      </div>
    </div>
  );
}