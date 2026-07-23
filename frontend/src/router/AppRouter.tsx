import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { AppLayout } from "@/layouts/AppLayout";
import { Dashboard } from "@/pages/Dashboard";
import { Channels } from "@/pages/Channels";
import { Guide } from "@/pages/Guide";
import { Favorites } from "@/pages/Favorites";
import { Settings } from "@/pages/Settings";
import { Watch } from "@/pages/Watch";

export const AppRouter: React.FC = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<AppLayout />}>
          <Route index element={<Dashboard />} />
          <Route path="channels" element={<Channels />} />
          <Route path="guide" element={<Guide />} />
          <Route path="favorites" element={<Favorites />} />
          <Route path="settings" element={<Settings />} />
          <Route path="watch/:id" element={<Watch />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
};

export default AppRouter;