import { Link } from "react-router-dom";

const menuItems = [
  { label: "Dashboard", path: "/" },
  { label: "Transactions", path: "/transactions" },
  { label: "Uploads", path: "/uploads" },
  { label: "Reviews", path: "/reviews" },
  { label: "Analytics", path: "/analytics" },
  { label: "Research", path: "/research" },
  { label: "AI Analyst", path: "/ai-analyst" },
  { label: "Reports", path: "/reports" },
  { label: "Simulator", path: "/simulator" },
  { label: "Alerts", path: "/alerts" },
  { label: "Audit", path: "/audit" },
];

export default function Sidebar() {
  return (
    <aside className="w-64 bg-slate-900 text-white min-h-screen">
      <div className="p-6 border-b border-slate-700">
        <h1 className="text-xl font-bold">VERIS</h1>
        <p className="text-xs text-slate-400">
          Unified Risk Score Platform
        </p>
      </div>

      <nav className="p-4 space-y-2">
        {menuItems.map((item) => (
          <Link
            key={item.path}
            to={item.path}
            className="block px-3 py-2 rounded hover:bg-slate-800"
          >
            {item.label}
          </Link>
        ))}
      </nav>
    </aside>
  );
}