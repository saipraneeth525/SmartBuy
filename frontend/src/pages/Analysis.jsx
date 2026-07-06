import MainLayout from "../layouts/MainLayout";

import ProductCard from "../components/product/ProductCard";
import PriceStats from "../components/product/PriceStats";
import PriceChart from "../components/product/PriceChart";
import RecommendationCard from "../components/product/RecommendationCard";
import InsightCard from "../components/product/InsightCard";
import ReviewCard from "../components/product/ReviewCard";

function Analysis() {
  return (
    <MainLayout>

      <div className="space-y-8">

        <ProductCard />

        <PriceStats />

        <PriceChart />

        <div className="grid lg:grid-cols-2 gap-8">

          <InsightCard />

          <RecommendationCard />

        </div>

        <ReviewCard />

      </div>

    </MainLayout>
  );
}

export default Analysis;