
export const frontendIntegration = [

    {
        module: "Business Day",
        page: "BusinessDay.jsx",
        route: "/business-day",
        backend: "business_days",
        status: "READY"
    },

    {
        module: "Pump Shift",
        page: "PumpShift.jsx",
        route: "/pump-shift",
        backend: "pump_shifts",
        status: "READY"
    },

    {
        module: "Meter Sales",
        page: "FuelSales.jsx",
        route: "/fuel-sales",
        backend: "meter_sales",
        status: "READY"
    },

    {
        module: "Cash Declaration",
        page: "CashDeclaration.jsx",
        route: "/cash-declaration",
        backend: "cash_declarations",
        status: "READY"
    },

    {
        module: "Reconciliation",
        page: "Reconciliation.jsx",
        route: "/reconciliation",
        backend: "reconciliations",
        status: "READY"
    },

    {
        module: "Manager Approval",
        page: "ManagerApproval.jsx",
        route: "/manager-approval",
        backend: "manager_approvals",
        status: "READY"
    },

    {
        module: "Fraud Dashboard",
        page: "FraudDashboard.jsx",
        route: "/fraud-dashboard",
        backend: "fraud_alerts",
        status: "READY"
    },

    {
        module: "Operational Reports",
        page: "OperationalReports.jsx",
        route: "/reports",
        backend: "operational_reports",
        status: "READY"
    }

];
