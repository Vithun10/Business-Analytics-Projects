import axios from "axios";

export const api = axios.create({
  baseURL: "http://127.0.0.1:8000/api/v1",
});

api.interceptors.request.use((config) => {
  config.headers["x-role"] = "admin";
  return config;
});