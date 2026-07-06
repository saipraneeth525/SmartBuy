import recentAnalyses from "../../data/recentAnalyses";

function RecentAnalyses() {
  return (
<div className="bg-white rounded-2xl border border-slate-200 shadow-sm p-6 transition-all duration-300 hover:-translate-y-1 hover:shadow-xl">
      <h2 className="text-2xl font-bold text-slate-800 mb-6">
        Recent Analyses
      </h2>

      <div className="space-y-4">

        {recentAnalyses.map((item) => (

          <div
            key={item.id}
className="
flex justify-between items-center
border rounded-xl p-4
hover:bg-slate-50
hover:-translate-y-1
hover:shadow-lg
transition-all
duration-300
"          >

            <div>

              <h3 className="font-semibold">
                {item.product}
              </h3>

              <p className="text-slate-500 text-sm">
                {item.time}
              </p>

            </div>

            <div className="text-right">

              <p className="font-bold">
                {item.price}
              </p>

              <span
                className={`
                  text-xs
                  font-semibold
                  px-3
                  py-1
                  rounded-full
                  ${
                    item.status === "BUY NOW"
                      ? "bg-green-100 text-green-700"
                      : item.status === "WAIT"
                      ? "bg-orange-100 text-orange-700"
                      : "bg-blue-100 text-blue-700"
                  }
                `}
              >
                {item.status}
              </span>

            </div>

          </div>

        ))}

      </div>

    </div>
  );
}

export default RecentAnalyses;