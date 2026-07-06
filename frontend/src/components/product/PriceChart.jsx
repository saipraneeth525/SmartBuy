import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  CartesianGrid,
} from "recharts";

import priceHistory from "../../data/priceHistory";

function PriceChart() {
  return (
<div className="bg-white rounded-2xl border border-slate-200 shadow-sm p-6 transition-all duration-300 hover:-translate-y-1 hover:shadow-xl">      <h2 className="text-xl font-semibold text-slate-800 mb-6">
        Price History
      </h2>

      <div className="h-80">
        <ResponsiveContainer width="100%" height="100%">
          <LineChart data={priceHistory}>
            <CartesianGrid strokeDasharray="3 3" />

            <XAxis dataKey="day" />

            <YAxis />

            <Tooltip />

            <Line
              type="monotone"
              dataKey="price"
              stroke="#7C3AED"
              strokeWidth={3}
            />
          </LineChart>
        </ResponsiveContainer>
      </div>

    </div>
  );
}

export default PriceChart;