import { useEffect } from "react";
import { Navigate, Route, Routes } from "react-router-dom";
import { useSession } from "./store/session";
import { Rail } from "./components/Rail";
import { NewRun } from "./screens/NewRun";
import { LiveRun } from "./screens/LiveRun";
import { Explorer } from "./screens/Explorer";
import { TestCases } from "./screens/TestCases";
import { History } from "./screens/History";

export default function App() {
  const detect = useSession((s) => s.detect);
  useEffect(() => {
    detect();
  }, [detect]);

  return (
    <div className="bg-ground flex h-full w-full overflow-hidden text-ink">
      <Rail />
      <main className="flex min-w-0 grow flex-col overflow-hidden">
        <Routes>
          <Route path="/" element={<NewRun />} />
          <Route path="/live" element={<LiveRun />} />
          <Route path="/graph" element={<Explorer />} />
          <Route path="/cases" element={<TestCases />} />
          <Route path="/history" element={<History />} />
          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </main>
    </div>
  );
}
