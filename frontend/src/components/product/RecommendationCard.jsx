import recommendation from "../../data/recommendation";

function RecommendationCard() {
  return (
    <div className="bg-white rounded-2xl border border-slate-200 shadow-sm p-6 transition-all duration-300 hover:-translate-y-1 hover:shadow-xl">
      
      <h2 className="text-lg font-semibold text-slate-700">
        SmartBuy Recommendation
      </h2>

      <div className="mt-6">
        <span className="inline-block bg-green-100 text-green-700 px-4 py-2 rounded-full font-semibold">
          {recommendation.decision}
        </span>
      </div>

      <div className="mt-6 space-y-4">

        <div>
          <p className="text-slate-500">
            Confidence
          </p>

          <h3 className="text-3xl font-bold text-violet-600">
            {recommendation.confidence}%
          </h3>
        </div>

        <div>
          <p className="text-slate-500">
            Expected Savings
          </p>

          <h3 className="text-2xl font-semibold">
            ₹{recommendation.savings.toLocaleString()}
          </h3>
        </div>

        <div>
          <p className="text-slate-500">
            Best Time
          </p>

          <h3 className="font-semibold">
            {recommendation.bestTime}
          </h3>
        </div>

      </div>

      <div className="mt-8 border-t pt-5">

        <p className="text-slate-500 text-sm">
          {recommendation.reason}
        </p>

      </div>

    </div>
  );
}

export default RecommendationCard;