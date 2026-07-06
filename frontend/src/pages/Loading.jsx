import { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { LoaderCircle } from "lucide-react";

function Loading() {
  const navigate = useNavigate();

  useEffect(() => {
    const timer = setTimeout(() => {
      navigate("/analysis");
    }, 3000);

    return () => clearTimeout(timer);
  }, [navigate]);

  return (
    <div className="min-h-screen bg-slate-100 flex items-center justify-center px-6">

      <div className="bg-white rounded-3xl shadow-lg border border-slate-200 p-10 w-full max-w-lg text-center">

        <LoaderCircle
          className="mx-auto animate-spin text-violet-600"
          size={60}
        />

        <h1 className="text-3xl font-bold mt-8">
          Preparing your SmartBuy Report
        </h1>

        <p className="text-slate-500 mt-3">
          Please wait while SmartBuy analyzes the product.
        </p>

        <div className="mt-10 space-y-4 text-left">

          <div className="flex items-center gap-3">
            ✅
            <span>Fetching latest product details</span>
          </div>

          <div className="flex items-center gap-3">
            ✅
            <span>Comparing historical prices</span>
          </div>

          <div className="flex items-center gap-3">
            ✅
            <span>Generating AI recommendation</span>
          </div>

          <div className="flex items-center gap-3">
            ⏳
            <span>Preparing final report...</span>
          </div>

        </div>

      </div>

    </div>
  );
}

export default Loading;