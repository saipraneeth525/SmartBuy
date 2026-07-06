import { Bell, Search } from "lucide-react";
import { useLocation } from "react-router-dom";

function Header() {
  const location = useLocation();

  const pageTitles = {
    "/": {
      title: "Dashboard",
      subtitle: "Welcome back! Ready to make smarter buying decisions.",
    },
    "/analysis": {
      title: "SmartBuy Report",
      subtitle: "Complete product price analysis and recommendation.",
    },
    "/products": {
      title: "My Products",
      subtitle: "Track and manage all your saved products.",
    },
    "/notifications": {
      title: "Notifications",
      subtitle: "Stay updated with your latest price alerts.",
    },
    "/analytics": {
      title: "Analytics",
      subtitle: "Analyze your shopping patterns.",
    },
    "/profile": {
      title: "Profile",
      subtitle: "Manage your account information.",
    },
    "/settings": {
      title: "Settings",
      subtitle: "Customize your SmartBuy experience.",
    },
  };

  const currentPage = pageTitles[location.pathname] || {
    title: "SmartBuy",
    subtitle: "Your personal shopping assistant.",
  };

  return (
    <header className="h-20 bg-white border-b border-slate-200 flex items-center justify-between px-4 md:px-8">

      {/* Left Section */}
      <div>
        <h2 className="text-2xl font-bold text-slate-800">
          {currentPage.title}
        </h2>

        <p className="text-sm text-slate-500 mt-1">
          {currentPage.subtitle}
        </p>
      </div>

      {/* Right Section */}
      <div className="flex items-center gap-4">

        {/* Search Bar */}
        <div className="hidden md:flex items-center bg-slate-100 rounded-xl px-4 py-2 w-80 border border-transparent focus-within:border-violet-500 transition-all">

          <Search
            size={18}
            className="text-slate-400"
          />

          <input
            type="text"
            placeholder="Search products..."
            className="bg-transparent outline-none ml-2 w-full text-sm"
          />

        </div>

        {/* Notification */}
        <button className="relative p-3 rounded-xl hover:bg-slate-100 transition-all">

          <Bell size={20} />

          <span className="absolute top-2 right-2 w-2 h-2 bg-red-500 rounded-full"></span>

        </button>

        {/* Profile */}
        <div className="flex items-center gap-3">

          <div className="w-11 h-11 rounded-full bg-gradient-to-r from-violet-600 to-indigo-600 flex items-center justify-center text-white font-bold shadow-md">
            P
          </div>

          <div className="hidden md:block">
            <p className="font-semibold text-slate-800">
              Praneeth
            </p>

            <p className="text-xs text-slate-500">
              Smart Shopper
            </p>
          </div>

        </div>

      </div>

    </header>
  );
}

export default Header;