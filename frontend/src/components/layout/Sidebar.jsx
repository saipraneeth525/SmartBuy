import { NavLink } from "react-router-dom";
import {
  LayoutDashboard,
  Package,
  Bell,
  BarChart3,
  User,
  Settings,
  LogOut,
} from "lucide-react";

const menuItems = [
  {
    name: "Dashboard",
    path: "/",
    icon: LayoutDashboard,
  },
  {
    name: "My Products",
    path: "/products",
    icon: Package,
  },
  {
    name: "Notifications",
    path: "/notifications",
    icon: Bell,
  },
  {
    name: "Analytics",
    path: "/analytics",
    icon: BarChart3,
  },
  {
    name: "Profile",
    path: "/profile",
    icon: User,
  },
  {
    name: "Settings",
    path: "/settings",
    icon: Settings,
  },
];

function Sidebar() {
  return (
    <aside className="w-64 min-h-screen bg-white border-r border-slate-200 p-6 flex flex-col">

      {/* Logo */}
      <div className="mb-10">
       <div className="mb-2">
  <h1 className="text-3xl font-extrabold bg-gradient-to-r from-violet-600 to-indigo-600 bg-clip-text text-transparent">
    SmartBuy
  </h1>

  <p className="text-sm text-slate-500 mt-1 leading-5">
    Your Personal Shopping Intelligence
  </p>
</div>
      </div>

      {/* Navigation */}
      <nav className="flex flex-col gap-2">

        {menuItems.map((item) => {
          const Icon = item.icon;

          return (
            <NavLink
              key={item.name}
              to={item.path}
              className={({ isActive }) =>
  `flex items-center gap-3 px-4 py-3 rounded-xl font-medium transition-all duration-300 ${
    isActive
      ? "bg-violet-600 text-white shadow-md"
      : "text-slate-600 hover:bg-slate-100 hover:translate-x-1"
  }`
}
            >
              <Icon size={20} />
              {item.name}
            </NavLink>
          );
        })}

      </nav>

      {/* Logout */}

      <div className="mt-auto">

        <button className="flex items-center gap-3 px-4 py-3 rounded-xl hover:bg-red-50 text-red-500 w-full">

          <LogOut size={20} />

          Logout

        </button>

      </div>

    </aside>
  );
}

export default Sidebar;