import { api } from "../api/client";

export const uploadCsv = async (
  file: File
) => {
  const formData = new FormData();

  formData.append(
    "file",
    file,
    file.name
  );

  const response = await api.post(
    "/uploads",
    formData
  );

  return response.data;
};