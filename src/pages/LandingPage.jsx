import React from "react";

export default function LandingPage({ onLogin }) {
  const features = [
    {
      icon: "⛽",
      title: "Pump Control",
      text: "Track pump activity, meter readings and shift performance with clear operational records.",
    },
    {
      icon: "🛢️",
      title: "Tank Monitoring",
      text: "Monitor tank readings and identify unusual fuel movement before losses become expensive.",
    },
    {
      icon: "📊",
      title: "Daily Reconciliation",
      text: "Bring meters, fuel sales, cash declarations and operational records together.",
    },
    {
      icon: "🛡️",
      title: "Fraud Detection",
      text: "Surface suspicious activity and operational discrepancies using evidence-backed records.",
    },
    {
      icon: "🎥",
      title: "Evidence Capture",
      text: "Capture operational evidence directly as part of important station workflows.",
    },
    {
      icon: "👥",
      title: "Staff Accountability",
      text: "Give owners and managers clearer visibility into shifts, assignments and approvals.",
    },
  ];

  return (
    <div className="pg-landing">
      <style>{`
        * {
          box-sizing: border-box;
        }

        .pg-landing {
          min-height: 100vh;
          background:
            radial-gradient(circle at 10% 10%, rgba(255, 166, 0, .20), transparent 28%),
            radial-gradient(circle at 90% 20%, rgba(0, 210, 255, .18), transparent 30%),
            linear-gradient(135deg, #07111f 0%, #0b1930 48%, #07111f 100%);
          color: #fff;
          font-family: Inter, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
          overflow-x: hidden;
        }

        .pg-nav {
          width: min(1180px, calc(100% - 32px));
          margin: auto;
          padding: 22px 0;
          display: flex;
          justify-content: space-between;
          align-items: center;
        }

        .pg-brand {
          display: flex;
          align-items: center;
          gap: 10px;
          font-weight: 900;
          font-size: 23px;
          letter-spacing: -.5px;
        }

        .pg-logo {
          width: 42px;
          height: 42px;
          display: grid;
          place-items: center;
          border-radius: 13px;
          background: linear-gradient(135deg, #ff9d00, #ff5c35);
          box-shadow: 0 10px 30px rgba(255, 122, 0, .25);
        }

        .pg-login {
          border: 1px solid rgba(255,255,255,.22);
          background: rgba(255,255,255,.07);
          color: white;
          padding: 11px 19px;
          border-radius: 12px;
          font-weight: 700;
          cursor: pointer;
        }

        .pg-hero {
          width: min(1180px, calc(100% - 32px));
          margin: auto;
          padding: 72px 0 90px;
          display: grid;
          grid-template-columns: 1.05fr .95fr;
          gap: 55px;
          align-items: center;
        }

        .pg-badge {
          display: inline-flex;
          padding: 8px 13px;
          border-radius: 999px;
          background: rgba(255,166,0,.11);
          border: 1px solid rgba(255,166,0,.25);
          color: #ffd27a;
          font-size: 13px;
          font-weight: 800;
          margin-bottom: 20px;
        }

        .pg-hero h1 {
          font-size: clamp(43px, 6vw, 76px);
          line-height: .98;
          letter-spacing: -3px;
          margin: 0 0 24px;
          max-width: 720px;
        }

        .pg-gradient {
          background: linear-gradient(90deg, #ffb000, #ff6b35, #20d9ff);
          -webkit-background-clip: text;
          background-clip: text;
          color: transparent;
        }

        .pg-hero p {
          color: #b8c6d9;
          font-size: 18px;
          line-height: 1.7;
          max-width: 650px;
          margin-bottom: 30px;
        }

        .pg-actions {
          display: flex;
          gap: 13px;
          flex-wrap: wrap;
        }

        .pg-primary {
          border: 0;
          color: #08111d;
          background: linear-gradient(135deg, #ffb000, #ff7138);
          padding: 15px 24px;
          border-radius: 13px;
          font-weight: 900;
          font-size: 15px;
          cursor: pointer;
          box-shadow: 0 14px 35px rgba(255, 133, 0, .22);
        }

        .pg-secondary {
          border: 1px solid rgba(255,255,255,.18);
          color: white;
          background: rgba(255,255,255,.06);
          padding: 15px 24px;
          border-radius: 13px;
          font-weight: 800;
          font-size: 15px;
        }

        .pg-dashboard {
          position: relative;
          min-height: 400px;
          border: 1px solid rgba(255,255,255,.13);
          border-radius: 28px;
          background: linear-gradient(145deg, rgba(255,255,255,.12), rgba(255,255,255,.035));
          box-shadow: 0 30px 80px rgba(0,0,0,.35);
          padding: 22px;
          overflow: hidden;
          backdrop-filter: blur(18px);
        }

        .pg-dashboard:before {
          content: "";
          position: absolute;
          width: 240px;
          height: 240px;
          right: -80px;
          top: -90px;
          background: rgba(0,210,255,.18);
          filter: blur(50px);
          border-radius: 50%;
        }

        .pg-window {
          position: relative;
          z-index: 1;
          background: #f6f9fc;
          color: #122033;
          border-radius: 18px;
          padding: 17px;
          min-height: 350px;
        }

        .pg-window-top {
          display: flex;
          justify-content: space-between;
          align-items: center;
          margin-bottom: 18px;
        }

        .pg-dots {
          display: flex;
          gap: 5px;
        }

        .pg-dots span {
          width: 8px;
          height: 8px;
          border-radius: 50%;
          background: #c6d0da;
        }

        .pg-status {
          font-size: 11px;
          padding: 6px 9px;
          border-radius: 999px;
          background: #e5f8ed;
          color: #198754;
          font-weight: 800;
        }

        .pg-kpis {
          display: grid;
          grid-template-columns: repeat(3, 1fr);
          gap: 9px;
        }

        .pg-kpi {
          background: white;
          border: 1px solid #e4e9ef;
          border-radius: 12px;
          padding: 13px;
        }

        .pg-kpi small {
          color: #7a8795;
          font-size: 10px;
        }

        .pg-kpi strong {
          display: block;
          margin-top: 5px;
          font-size: 18px;
        }

        .pg-chart {
          margin-top: 12px;
          height: 155px;
          border-radius: 14px;
          background:
            linear-gradient(rgba(20,40,70,.06) 1px, transparent 1px),
            linear-gradient(90deg, rgba(20,40,70,.06) 1px, transparent 1px);
          background-size: 30px 30px;
          position: relative;
          overflow: hidden;
        }

        .pg-chart-line {
          position: absolute;
          left: 4%;
          right: 4%;
          bottom: 35%;
          height: 3px;
          background: linear-gradient(90deg, #ff9d00, #ff6635, #14c9db);
          transform: rotate(-5deg);
          box-shadow: 0 0 14px rgba(255,130,0,.35);
        }

        .pg-section {
          width: min(1180px, calc(100% - 32px));
          margin: auto;
          padding: 85px 0;
        }

        .pg-section-title {
          text-align: center;
          max-width: 760px;
          margin: 0 auto 45px;
        }

        .pg-section-title h2 {
          font-size: clamp(31px, 4vw, 48px);
          margin: 0 0 14px;
          letter-spacing: -1.5px;
        }

        .pg-section-title p {
          color: #9eafc3;
          line-height: 1.7;
        }

        .pg-features {
          display: grid;
          grid-template-columns: repeat(3, 1fr);
          gap: 17px;
        }

        .pg-feature {
          padding: 26px;
          border: 1px solid rgba(255,255,255,.10);
          background: rgba(255,255,255,.045);
          border-radius: 20px;
          transition: transform .2s ease, background .2s ease;
        }

        .pg-feature:hover {
          transform: translateY(-5px);
          background: rgba(255,255,255,.075);
        }

        .pg-icon {
          width: 48px;
          height: 48px;
          display: grid;
          place-items: center;
          border-radius: 14px;
          background: linear-gradient(135deg, rgba(255,176,0,.18), rgba(0,210,255,.13));
          font-size: 23px;
          margin-bottom: 17px;
        }

        .pg-feature h3 {
          margin: 0 0 9px;
          font-size: 19px;
        }

        .pg-feature p {
          color: #98aabd;
          line-height: 1.65;
          margin: 0;
          font-size: 14px;
        }

        .pg-cta {
          text-align: center;
          padding: 75px 25px;
          border-radius: 30px;
          background:
            radial-gradient(circle at 50% 0%, rgba(255,166,0,.18), transparent 42%),
            rgba(255,255,255,.045);
          border: 1px solid rgba(255,255,255,.11);
        }

        .pg-cta h2 {
          font-size: clamp(32px, 5vw, 52px);
          margin: 0 0 15px;
        }

        .pg-cta p {
          color: #aab9ca;
          max-width: 620px;
          margin: 0 auto 28px;
          line-height: 1.7;
        }

        .pg-footer {
          border-top: 1px solid rgba(255,255,255,.08);
          color: #74859a;
          text-align: center;
          padding: 28px 16px;
          font-size: 13px;
        }

        @media (max-width: 850px) {
          .pg-hero {
            grid-template-columns: 1fr;
            padding-top: 45px;
          }

          .pg-features {
            grid-template-columns: repeat(2, 1fr);
          }
        }

        @media (max-width: 560px) {
          .pg-nav {
            width: min(100% - 22px, 1180px);
          }

          .pg-hero,
          .pg-section {
            width: min(100% - 22px, 1180px);
          }

          .pg-hero {
            padding-top: 35px;
            padding-bottom: 55px;
          }

          .pg-hero h1 {
            letter-spacing: -2px;
          }

          .pg-features {
            grid-template-columns: 1fr;
          }

          .pg-kpis {
            grid-template-columns: 1fr;
          }

          .pg-dashboard {
            padding: 12px;
          }
        }
      `}</style>

      <header className="pg-nav">
        <div className="pg-brand">
          <div className="pg-logo">⛽</div>
          PetroGuard
        </div>

        <button className="pg-login" onClick={onLogin}>
          Login
        </button>
      </header>

      <main>
        <section className="pg-hero">
          <div>
            <div className="pg-badge">FUEL STATION CONTROL PLATFORM</div>

            <h1>
              Control every drop.
              <br />
              <span className="pg-gradient">Protect every sale.</span>
            </h1>

            <p>
              PetroGuard gives fuel station owners and managers powerful
              visibility over pumps, tanks, shifts, sales, reconciliation
              and operational evidence — all in one platform.
            </p>

            <div className="pg-actions">
              <button className="pg-primary" onClick={onLogin}>
                Get Started →
              </button>

              <div className="pg-secondary">
                Built for real station operations
              </div>
            </div>
          </div>

          <div className="pg-dashboard">
            <div className="pg-window">
              <div className="pg-window-top">
                <strong>PetroGuard Operations</strong>
                <div className="pg-status">● Station Online</div>
              </div>

              <div className="pg-kpis">
                <div className="pg-kpi">
                  <small>Fuel Sales</small>
                  <strong>₦285K</strong>
                </div>
                <div className="pg-kpi">
                  <small>Active Shifts</small>
                  <strong>04</strong>
                </div>
                <div className="pg-kpi">
                  <small>Variance</small>
                  <strong>0.8%</strong>
                </div>
              </div>

              <div className="pg-chart">
                <div className="pg-chart-line" />
              </div>
            </div>
          </div>
        </section>

        <section className="pg-section">
          <div className="pg-section-title">
            <h2>Everything you need to control your station</h2>
            <p>
              Turn daily station operations into clear, accountable and
              evidence-backed processes.
            </p>
          </div>

          <div className="pg-features">
            {features.map((feature) => (
              <article className="pg-feature" key={feature.title}>
                <div className="pg-icon">{feature.icon}</div>
                <h3>{feature.title}</h3>
                <p>{feature.text}</p>
              </article>
            ))}
          </div>
        </section>

        <section className="pg-section">
          <div className="pg-cta">
            <h2>Take control of your station.</h2>
            <p>
              Bring your pumps, tanks, people, sales and reconciliation
              together with PetroGuard.
            </p>
            <button className="pg-primary" onClick={onLogin}>
              Enter PetroGuard →
            </button>
          </div>
        </section>
      </main>

      <footer className="pg-footer">
        © {new Date().getFullYear()} PetroGuard. Fuel station control,
        accountability and loss prevention.
      </footer>
    </div>
  );
}
