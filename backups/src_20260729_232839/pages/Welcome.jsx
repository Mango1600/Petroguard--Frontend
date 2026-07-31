export default function Welcome({ staff, continueApp }) {
  return (
    <div style={{padding:20,maxWidth:500,margin:"auto"}}>
      <h1>⛽ PetroGuard</h1>
      <h2>Welcome 👋</h2>

      <hr />

      <p><b>Name:</b> {staff?.name}</p>
      <p><b>Role:</b> {staff?.role}</p>
      <p><b>Station:</b> {staff?.station_id}</p>

      <br />

      <button
        onClick={continueApp}
        style={{
          width:"100%",
          padding:12,
          fontSize:16
        }}
      >
        Continue
      </button>
    </div>
  );
}
