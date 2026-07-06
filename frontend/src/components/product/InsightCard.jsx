import recommendation from "../../data/recommendation";

function InsightCard() {
  return (
<div className="bg-white rounded-2xl border border-slate-200 shadow-sm p-6 transition-all duration-300 hover:-translate-y-1 hover:shadow-xl">     <p className="uppercase tracking-wider text-sm font-semibold opacity-80">
        SmartBuy Insight
      </p>

      <h2 className="text-3xl font-bold mt-3">
        Here's what we found.
      </h2>

      <p className="mt-5 text-violet-100 leading-8 text-lg">
        {recommendation.reason}
      </p>

      <div className="mt-8 flex gap-4">

        <div className="bg-white/15 px-5 py-3 rounded-xl">
          Confidence
          <h3 className="text-2xl font-bold mt-1">
            {recommendation.confidence}%
          </h3>
        </div>

        <div className="bg-white/15 px-5 py-3 rounded-xl">
          Decision
          <h3 className="text-2xl font-bold mt-1">
            {recommendation.decision}
          </h3>
        </div>

      </div>

    </div>
  );
}

export default InsightCard;