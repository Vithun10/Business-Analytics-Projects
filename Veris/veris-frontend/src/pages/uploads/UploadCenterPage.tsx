import { useState } from "react";
import { uploadCsv } from "../../services/uploadService";

export default function UploadCenterPage() {
  const [file, setFile] = useState<File | null>(null);
  const [message, setMessage] = useState("");
  const [loading, setLoading] = useState(false);

  const uploadFile = async () => {
    if (!file) {
      setMessage("Please select a CSV file.");
      return;
    }

    try {
      setLoading(true);

      const response = await uploadCsv(file);

      setMessage(
        `Upload successful. Batch ID: ${response.batch_id}`
      );
    } catch (error: any) {
      console.error(error);

      if (error?.response?.data) {
        setMessage(
          JSON.stringify(
            error.response.data,
            null,
            2
          )
        );
      } else {
        setMessage("Upload failed");
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="p-6">
      <h1 className="text-4xl font-bold mb-6">
        Upload Center
      </h1>

      <div className="bg-white p-6 rounded-xl shadow max-w-xl">

        <input
          type="file"
          accept=".csv"
          onChange={(e) =>
            setFile(
              e.target.files?.[0] || null
            )
          }
          className="mb-4"
        />

        <button
          onClick={uploadFile}
          disabled={loading}
          className="bg-blue-600 text-white px-4 py-2 rounded"
        >
          {loading
            ? "Uploading..."
            : "Upload CSV"}
        </button>

        {message && (
          <pre className="mt-4 text-sm whitespace-pre-wrap">
            {message}
          </pre>
        )}

      </div>
    </div>
  );
}