import MainLayout from "../layouts/MainLayout";
import WelcomeSection from "../components/dashboard/WelcomeSection";
import UrlInput from "../components/dashboard/UrlInput";
import RecentAnalyses from "../components/dashboard/RecentAnalyses";

function Dashboard() {
  return (
    <MainLayout>
      <WelcomeSection />
      <UrlInput />
      <RecentAnalyses />
    </MainLayout>
  );
}

export default Dashboard;