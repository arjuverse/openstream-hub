import { Navigate, Route, Routes } from "react-router-dom";

import Dashboard from "@/pages/Dashboard";
import Channels from "@/pages/Channels";
import Guide from "@/pages/Guide";
import Favorites from "@/pages/Favorites";
import Settings from "@/pages/Settings";

export default function AppRouter() {
  return (
    <Routes>
      <Route path="/" element={<Navigate to="/dashboard" replace />} />

      <Route path="/dashboard" element={<Dashboard />} />
      <Route path="/channels" element={<Channels />} />
      <Route path="/guide" element={<Guide />} />
      <Route path="/favorites" element={<Favorites />} />
      <Route path="/settings" element={<Settings />} />
    </Routes>
  );
}