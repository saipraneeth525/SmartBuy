import { useNavigate } from "react-router-dom";
import { Search } from "lucide-react";

function UrlInput() {

  const navigate = useNavigate();

  return (
    <section className="w-full p-3 outline-none rounded-xl transition-all focus:ring-2 focus:ring-violet-500">

      <h2 className="text-xl font-semibold text-slate-800">
        Analyze a Product
      </h2>

      <p className="text-slate-500 mt-2">
        Paste an Amazon or Flipkart product link below.
      </p>

<div className="flex flex-col md:flex-row gap-4 mt-6">
        <div className="flex items-center flex-1 border rounded-xl px-4">

          <Search className="text-slate-400" size={20} />

          <input
            type="text"
            placeholder="Paste product URL here..."
className="w-full p-3 outline-none transition-all focus:ring-2 focus:ring-violet-500 rounded-xl"          />

        </div>

        <button
  onClick={() => navigate("/loading")}
  className="
w-full md:w-auto
bg-violet-600
hover:bg-violet-700
hover:scale-[1.02]
transition-all
duration-300
text-white
px-6
py-3
rounded-xl
font-medium
shadow-md
hover:shadow-lg
"
>
  Analyze with SmartBuy
</button>
          
      </div>

    </section>
  );
}

export default UrlInput;