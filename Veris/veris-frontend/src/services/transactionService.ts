import {api} from "../api/client";

export const getTransactions = async () => {
  const response = await api.get("/transactions?page=1&page_size=1000")
  return response.data;
};