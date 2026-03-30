import { useState, useEffect, useCallback } from "react";

const CATEGORIES = ["Hauts", "Bas", "Robes", "Vestes", "Chaussures", "Accessoires", "Autre"];
const PLATFORMS = ["Vinted", "Autre"];
const LOT_COLORS = ["#6c8ff0", "#e0a84a", "#4ecf8a", "#e07878", "#b07de0", "#4ecfcf", "#e0d45a"];
const PIE_COLORS = ["#6c8ff0","#4ecf8a","#e0a84a","#e07878","#b07de0","#4ecfcf","#e0d45a","#f07cc0","#70c4e0","#e08840","#a0d060","#c070e0"];

const D = {
  bg: "#0f0f14", card: "#1a1a24", card2: "#22222f",
  border: "#2a2a3a", text: "#e8e4f0", muted: "#7a7898", accent: "#6c8ff0",
};

const DEMO_LOTS = [
  { id: "lot-1", name: "Commande Vinted Mars", date: "2026-03-01", color: "#6c8ff0" },
  { id: "lot-2", name: "Lot friperie Février", date: "2026-02-15", color: "#e0a84a" },
];
const DEMO_ITEMS = [
  { id: 1,  name: "Blazer Zara oversize",        category: "Vestes", brand: "Zara",            buyPrice: 12, fees: 1.5, sellPrice: 38, platform: "Vinted", status: "Vendu",    date: "2026-03-01", sellDate: "2026-03-10", lotId: "lot-1" },
  { id: 2,  name: "Jean vintage Levi's 501",      category: "Bas",    brand: "Levi's",           buyPrice: 8,  fees: 1,   sellPrice: 29, platform: "Vinted", status: "Vendu",    date: "2026-03-05", sellDate: "2026-03-18", lotId: "lot-1" },
  { id: 3,  name: "Pull maille crème",            category: "Hauts",  brand: "H&M",             buyPrice: 5,  fees: 0.8, sellPrice: null, platform: "Vinted", status: "En stock", date: "2026-03-20", sellDate: null,        lotId: "lot-1" },
  { id: 4,  name: "Robe fleurie Other Stories",   category: "Robes",  brand: "& Other Stories", buyPrice: 15, fees: 2,   sellPrice: 42, platform: "Vinted", status: "Vendu",    date: "2026-02-15", sellDate: "2026-03-02", lotId: "lot-2" },
  { id: 5,  name: "Veste en jean Levi's femme",   category: "Vestes", brand: "Levi's",           buyPrice: 10, fees: 1,   sellPrice: null, platform: "Vinted", status: "En stock", date: "2026-02-15", sellDate: null,        lotId: "lot-2" },
  { id: 6,  name: "T-shirt Levi's blanc",         category: "Hauts",  brand: "Levi's",           buyPrice: 6,  fees: 0.8, sellPrice: 18, platform: "Vinted", status: "Vendu",    date: "2026-03-10", sellDate: "2026-03-22", lotId: "lot-1" },
  { id: 7,  name: "Hoodie Zara homme",            category: "Hauts",  brand: "Zara",            buyPrice: 9,  fees: 1,   sellPrice: 24, platform: "Vinted", status: "Vendu",    date: "2026-02-20", sellDate: "2026-03-05", lotId: "lot-2" },
];

// ─── localStorage helpers ─────────────────────────────────────────────────────
function loadLS(key, fallback) {
  try { const v = localStorage.getItem(key); return v ? JSON.parse(v) : fallback; } catch { return fallback; }
}
function saveLS(key, value) {
  try { localStorage.setItem(key, JSON.stringify(value)); } catch {}
}

function formatEur(n) {
  if (n === null || n === undefined || isNaN(n)) return "—";
  return n.toLocaleString("fr-FR", { style: "currency", currency: "EUR" });
}
const EMOJI = { "Vestes":"🧥","Bas":"👖","Hauts":"👕","Robes":"👗","Chaussures":"👟","Accessoires":"👜","Autre":"📦" };

// ─── Export CSV ───────────────────────────────────────────────────────────────
function exportCSV(items, lots) {
  const getLot = (id) => lots.find(l => l.id === id);
  const headers = ["Nom","Marque","Catégorie","Plateforme","Commande","Date achat","Prix achat","Frais","Prix vente","Bénéfice","Marge %","Statut","Date vente"];
  const rows = items.map(i => {
    const cost = i.buyPrice + i.fees;
    const profit = i.sellPrice !== null ? i.sellPrice - cost : "";
    const margin = i.sellPrice !== null ? ((profit / cost) * 100).toFixed(1) : "";
    const lot = getLot(i.lotId);
    return [i.name, i.brand||"", i.category, i.platform, lot?.name||"", i.date, i.buyPrice, i.fees, i.sellPrice||"", profit, margin, i.status, i.sellDate||""];
  });
  const csv = [headers, ...rows].map(r => r.map(v => `"${String(v).replace(/"/g,'""')}"`).join(",")).join("\n");
  const blob = new Blob(["\uFEFF" + csv], { type: "text/csv;charset=utf-8;" });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a"); a.href = url; a.download = "resellbook_export.csv"; a.click();
  URL.revokeObjectURL(url);
}

// ─── Graphique CA ─────────────────────────────────────────────────────────────
function LineChart({ items }) {
  const sold = items.filter(i => i.status === "Vendu" && i.sellDate);
  if (sold.length === 0) return <div style={{ color: D.muted, textAlign: "center", padding: 32 }}>Aucune vente enregistrée</div>;

  // Regrouper par mois
  const byMonth = {};
  sold.forEach(i => {
    const key = i.sellDate.slice(0, 7); // YYYY-MM
    if (!byMonth[key]) byMonth[key] = { ca: 0, benef: 0, count: 0 };
    byMonth[key].ca += i.sellPrice || 0;
    byMonth[key].benef += (i.sellPrice || 0) - i.buyPrice - i.fees;
    byMonth[key].count += 1;
  });

  const months = Object.keys(byMonth).sort();
  const caValues = months.map(m => byMonth[m].ca);
  const benefValues = months.map(m => byMonth[m].benef);
  const allValues = [...caValues, ...benefValues, 0];
  const maxVal = Math.max(...allValues);
  const minVal = Math.min(...allValues, 0);
  const range = maxVal - minVal || 1;

  const W = 520, H = 180, PL = 50, PR = 16, PT = 16, PB = 36;
  const chartW = W - PL - PR, chartH = H - PT - PB;
  const n = months.length;

  function x(i) { return PL + (n === 1 ? chartW / 2 : (i / (n - 1)) * chartW); }
  function y(v) { return PT + chartH - ((v - minVal) / range) * chartH; }

  function polyline(values, color) {
    if (values.length < 2) return null;
    const pts = values.map((v, i) => `${x(i)},${y(v)}`).join(" ");
    return <polyline points={pts} fill="none" stroke={color} strokeWidth="2.5" strokeLinejoin="round" strokeLinecap="round" />;
  }

  function area(values, color) {
    if (values.length < 2) return null;
    const pts = values.map((v, i) => `${x(i)},${y(v)}`).join(" ");
    const base = y(0);
    return <polygon points={`${x(0)},${base} ${pts} ${x(n-1)},${base}`} fill={color} opacity="0.10" />;
  }

  // Graduations Y
  const steps = 4;
  const yTicks = Array.from({ length: steps + 1 }, (_, i) => minVal + (range / steps) * i);

  const [tooltip, setTooltip] = useState(null);

  return (
    <div style={{ overflowX: "auto" }}>
      <svg width={W} height={H} style={{ display: "block", minWidth: 300 }}
        onMouseLeave={() => setTooltip(null)}>
        {/* Grille */}
        {yTicks.map((v, i) => (
          <g key={i}>
            <line x1={PL} y1={y(v)} x2={W - PR} y2={y(v)} stroke={D.border} strokeWidth="1" />
            <text x={PL - 6} y={y(v) + 4} textAnchor="end" fill={D.muted} fontSize="10">{v >= 1000 ? `${(v/1000).toFixed(1)}k` : v.toFixed(0)}€</text>
          </g>
        ))}
        {/* Ligne zéro si négatifs */}
        {minVal < 0 && <line x1={PL} y1={y(0)} x2={W - PR} y2={y(0)} stroke={D.accent} strokeWidth="1" strokeDasharray="4,3" opacity="0.4" />}
        {/* Aires */}
        {area(caValues, "#6c8ff0")}
        {area(benefValues, "#4ecf8a")}
        {/* Lignes */}
        {polyline(caValues, "#6c8ff0")}
        {polyline(benefValues, "#4ecf8a")}
        {/* Points + labels mois */}
        {months.map((m, i) => (
          <g key={m}>
            <circle cx={x(i)} cy={y(caValues[i])} r="4" fill="#6c8ff0" />
            <circle cx={x(i)} cy={y(benefValues[i])} r="4" fill="#4ecf8a" />
            {/* Zone invisible pour le hover */}
            <rect x={x(i) - 16} y={PT} width={32} height={chartH} fill="transparent" style={{ cursor: "pointer" }}
              onMouseEnter={() => setTooltip({ i, m, ca: caValues[i], benef: benefValues[i], count: byMonth[m].count })} />
            <text x={x(i)} y={H - 6} textAnchor="middle" fill={D.muted} fontSize="10">{m.slice(5)}/{m.slice(2,4)}</text>
          </g>
        ))}
        {/* Tooltip */}
        {tooltip && (() => {
          const tx = Math.min(x(tooltip.i), W - 130); const ty = PT + 4;
          return (
            <g>
              <line x1={x(tooltip.i)} y1={PT} x2={x(tooltip.i)} y2={H - PB} stroke={D.muted} strokeWidth="1" strokeDasharray="3,3" />
              <rect x={tx + 8} y={ty} width={115} height={62} rx="6" fill={D.card2} stroke={D.border} />
              <text x={tx + 16} y={ty + 16} fill={D.text} fontSize="11" fontWeight="700">{tooltip.m} · {tooltip.count} vente{tooltip.count > 1 ? "s" : ""}</text>
              <circle cx={tx + 16} cy={ty + 30} r="4" fill="#6c8ff0" />
              <text x={tx + 24} y={ty + 34} fill={D.text} fontSize="10">CA : {formatEur(tooltip.ca)}</text>
              <circle cx={tx + 16} cy={ty + 46} r="4" fill="#4ecf8a" />
              <text x={tx + 24} y={ty + 50} fill={D.text} fontSize="10">Bénéf : {formatEur(tooltip.benef)}</text>
            </g>
          );
        })()}
      </svg>
      {/* Légende */}
      <div style={{ display: "flex", gap: 16, marginTop: 8, paddingLeft: PL }}>
        <div style={{ display: "flex", alignItems: "center", gap: 6, fontSize: "12px", color: D.muted }}><div style={{ width: 12, height: 3, background: "#6c8ff0", borderRadius: 2 }} />CA</div>
        <div style={{ display: "flex", alignItems: "center", gap: 6, fontSize: "12px", color: D.muted }}><div style={{ width: 12, height: 3, background: "#4ecf8a", borderRadius: 2 }} />Bénéfice</div>
      </div>
    </div>
  );
}

// ─── Composants de base ───────────────────────────────────────────────────────
function LotStatusBadge({ ca, cost, benef }) {
  let label, color, bg, border;
  if (benef > 0) { label = "✓ Positif"; color = "#4ecf8a"; bg = "#4ecf8a22"; border = "1px solid #4ecf8a44"; }
  else if (ca >= cost) { label = "⟳ Remboursé"; color = "#6c8ff0"; bg = "#6c8ff022"; border = "1px solid #6c8ff044"; }
  else { label = "✗ Négatif"; color = "#e07878"; bg = "#e0787822"; border = "1px solid #e0787844"; }
  return <span style={{ display: "inline-block", padding: "4px 12px", borderRadius: "999px", fontSize: "12px", fontWeight: 800, color, background: bg, border, whiteSpace: "nowrap" }}>{label}</span>;
}

function Badge({ status }) {
  return <span style={{ display: "inline-block", padding: "2px 10px", borderRadius: "999px", fontSize: "11px", fontWeight: 700, background: status === "Vendu" ? "rgba(78,207,138,0.15)" : "rgba(224,168,74,0.15)", color: status === "Vendu" ? "#4ecf8a" : "#e0a84a", border: status === "Vendu" ? "1px solid rgba(78,207,138,0.35)" : "1px solid rgba(224,168,74,0.35)" }}>{status}</span>;
}

function StatCard({ label, value, sub, accent }) {
  return (
    <div style={{ background: D.card, borderRadius: "16px", padding: "20px 22px", borderLeft: `4px solid ${accent}`, minWidth: 0, flex: 1 }}>
      <div style={{ fontSize: "11px", color: D.muted, fontWeight: 600, letterSpacing: "0.08em", marginBottom: 6, textTransform: "uppercase" }}>{label}</div>
      <div style={{ fontSize: "24px", fontWeight: 800, color: D.text, lineHeight: 1.1 }}>{value}</div>
      {sub && <div style={{ fontSize: "12px", color: D.muted, marginTop: 4 }}>{sub}</div>}
    </div>
  );
}

function Modal({ open, onClose, wide, children }) {
  if (!open) return null;
  return (
    <div onClick={onClose} style={{ position: "fixed", inset: 0, background: "rgba(0,0,0,0.75)", zIndex: 1000, display: "flex", alignItems: "center", justifyContent: "center", padding: 16 }}>
      <div onClick={e => e.stopPropagation()} style={{ background: D.card, borderRadius: "20px", padding: "28px 26px", width: wide ? "min(98vw,780px)" : "min(95vw,500px)", border: `1px solid ${D.border}`, maxHeight: "92vh", overflowY: "auto" }}>
        {children}
      </div>
    </div>
  );
}

function PieChart({ data }) {
  const [hovered, setHovered] = useState(null);
  const total = data.reduce((s, d) => s + d.value, 0);
  if (total === 0) return <div style={{ color: D.muted, textAlign: "center", padding: 32 }}>Aucune donnée</div>;
  const size = 200, cx = size/2, cy = size/2, r = 78, inner = 44;
  let angle = -Math.PI/2;
  const slices = data.map(d => { const sweep = (d.value/total)*2*Math.PI; const sa = angle; angle += sweep; return {...d, sa, sweep, ea: angle}; });
  function arc(sa,ea,R,ri) {
    const x1=cx+R*Math.cos(sa),y1=cy+R*Math.sin(sa),x2=cx+R*Math.cos(ea),y2=cy+R*Math.sin(ea),x3=cx+ri*Math.cos(ea),y3=cy+ri*Math.sin(ea),x4=cx+ri*Math.cos(sa),y4=cy+ri*Math.sin(sa);
    return `M${x1},${y1} A${R},${R},0,${ea-sa>Math.PI?1:0},1,${x2},${y2} L${x3},${y3} A${ri},${ri},0,${ea-sa>Math.PI?1:0},0,${x4},${y4} Z`;
  }
  return (
    <div style={{ display: "flex", gap: 20, alignItems: "center", flexWrap: "wrap" }}>
      <svg width={size} height={size} style={{ flexShrink: 0 }}>
        {slices.map((s,i) => { const isH=hovered===i; const mid=s.sa+s.sweep/2; const off=isH?7:0; return <path key={i} d={arc(s.sa,s.ea,r,inner)} fill={s.color} transform={`translate(${off*Math.cos(mid)},${off*Math.sin(mid)})`} style={{cursor:"pointer",transition:"transform 0.12s",opacity:hovered!==null&&hovered!==i?0.45:1}} onMouseEnter={()=>setHovered(i)} onMouseLeave={()=>setHovered(null)} />; })}
        {hovered!==null?(<><text x={cx} y={cy-7} textAnchor="middle" fill={D.text} fontSize="12" fontWeight="800">{slices[hovered].label}</text><text x={cx} y={cy+9} textAnchor="middle" fill={slices[hovered].color} fontSize="12" fontWeight="700">{slices[hovered].value}</text><text x={cx} y={cy+24} textAnchor="middle" fill={D.muted} fontSize="10">{((slices[hovered].value/total)*100).toFixed(1)}%</text></>):(<><text x={cx} y={cy-2} textAnchor="middle" fill={D.text} fontSize="20" fontWeight="800">{total}</text><text x={cx} y={cy+14} textAnchor="middle" fill={D.muted} fontSize="10">ventes</text></>)}
      </svg>
      <div style={{ flex:1, minWidth:130, display:"flex", flexDirection:"column", gap:7 }}>
        {[...slices].sort((a,b)=>b.value-a.value).map((s,i)=>(
          <div key={i} onMouseEnter={()=>setHovered(slices.indexOf(s))} onMouseLeave={()=>setHovered(null)} style={{display:"flex",alignItems:"center",gap:7,cursor:"pointer",opacity:hovered!==null&&hovered!==slices.indexOf(s)?0.4:1,transition:"opacity 0.12s"}}>
            <div style={{width:9,height:9,borderRadius:"50%",background:s.color,flexShrink:0}}/>
            <span style={{fontSize:"12px",color:D.text,fontWeight:600,flex:1}}>{s.label}</span>
            <span style={{fontSize:"11px",color:D.muted}}>{s.value}</span>
            <span style={{fontSize:"10px",color:s.color,fontWeight:700,minWidth:34,textAlign:"right"}}>{((s.value/total)*100).toFixed(0)}%</span>
          </div>
        ))}
      </div>
    </div>
  );
}

const inp = { width:"100%", padding:"9px 12px", borderRadius:"9px", border:`1.5px solid ${D.border}`, fontSize:"13px", fontFamily:"inherit", background:D.card2, outline:"none", boxSizing:"border-box", marginTop:"3px", color:D.text };
const lbl = { fontSize:"11px", fontWeight:700, color:D.muted, letterSpacing:"0.07em", textTransform:"uppercase" };

function ArticleLine({ line, onChange, onRemove, canRemove }) {
  return (
    <div style={{ background:D.card2, borderRadius:"12px", padding:"14px", border:`1px solid ${D.border}`, position:"relative" }}>
      {canRemove && <button onClick={onRemove} style={{ position:"absolute", top:10, right:10, background:"#e0787822", color:"#e07878", border:"1px solid #e0787844", borderRadius:"6px", width:24, height:24, cursor:"pointer", fontWeight:800, fontSize:"12px" }}>✕</button>}
      <div style={{ display:"grid", gridTemplateColumns:"1fr 1fr", gap:10, marginBottom:10 }}>
        <div style={{ gridColumn:"1/-1" }}><label style={lbl}>Nom</label><input style={inp} placeholder="Ex: Jean Levi's 501 homme" value={line.name} onChange={e=>onChange({...line,name:e.target.value})} /></div>
        <div><label style={lbl}>Marque</label><input style={inp} placeholder="Ex: Levi's" value={line.brand} onChange={e=>onChange({...line,brand:e.target.value})} /></div>
        <div><label style={lbl}>Catégorie</label><select style={inp} value={line.category} onChange={e=>onChange({...line,category:e.target.value})}>{CATEGORIES.map(c=><option key={c}>{c}</option>)}</select></div>
        <div><label style={lbl}>Quantité</label><input style={{...inp,fontWeight:800,color:D.accent}} type="number" min="1" max="999" value={line.qty} onChange={e=>onChange({...line,qty:e.target.value})} /></div>
        <div><label style={lbl}>Prix unitaire (€)</label><input style={inp} type="number" placeholder="0.00" value={line.buyPrice} onChange={e=>onChange({...line,buyPrice:e.target.value})} /></div>
        <div><label style={lbl}>Frais unitaires (€)</label><input style={inp} type="number" placeholder="0.00" value={line.fees} onChange={e=>onChange({...line,fees:e.target.value})} /></div>
      </div>
      {line.name && line.qty && line.buyPrice && (
        <div style={{ background:D.card, borderRadius:"8px", padding:"8px 12px", fontSize:"12px", display:"flex", justifyContent:"space-between", border:`1px solid ${D.border}` }}>
          <span style={{color:D.muted}}>{parseInt(line.qty)||0} pièce{parseInt(line.qty)>1?"s":""} × {formatEur((parseFloat(line.buyPrice)||0)+(parseFloat(line.fees)||0))}</span>
          <span style={{fontWeight:800,color:D.accent}}>{formatEur(((parseFloat(line.buyPrice)||0)+(parseFloat(line.fees)||0))*(parseInt(line.qty)||0))}</span>
        </div>
      )}
    </div>
  );
}

function newLine() { return { _id: Math.random(), name:"", brand:"", category:"Hauts", qty:"1", buyPrice:"", fees:"" }; }

let _nextId = 20;
let _nextLotId = 3;

// ─── APP ─────────────────────────────────────────────────────────────────────
export default function App() {
  const [items, setItems] = useState(() => loadLS("rb_items", DEMO_ITEMS));
  const [lots,  setLots]  = useState(() => loadLS("rb_lots",  DEMO_LOTS));
  const [nextId,    setNextId]    = useState(() => loadLS("rb_nextId",    20));
  const [nextLotId, setNextLotId] = useState(() => loadLS("rb_nextLotId", 3));
  const [saved, setSaved] = useState(false);

  const [tab, setTab] = useState("dashboard");
  const [addItemModal, setAddItemModal] = useState(false);
  const [sellModal, setSellModal]   = useState(null);
  const [dupModal,  setDupModal]    = useState(null);
  const [lotModal,  setLotModal]    = useState(false);
  const [selectedLot, setSelectedLot] = useState(null);
  const [filterStatus, setFilterStatus] = useState("Tous");
  const [filterCat,    setFilterCat]    = useState("Toutes");
  const [filterLot,    setFilterLot]    = useState("Tous");
  const [form,     setForm]     = useState({ name:"", category:"Hauts", brand:"", buyPrice:"", fees:"", platform:"Vinted", date:new Date().toISOString().slice(0,10), lotId:"" });
  const [sellForm, setSellForm] = useState({ sellPrice:"", sellDate:new Date().toISOString().slice(0,10) });
  const [dupForm,  setDupForm]  = useState({ quantity:"2", buyPrice:"", fees:"", lotId:"" });
  const [lotForm,  setLotForm]  = useState({ name:"", date:new Date().toISOString().slice(0,10), color:LOT_COLORS[0], platform:"Vinted" });
  const [lotLines, setLotLines] = useState([newLine()]);

  // ─── Sauvegarde automatique ──────────────────────────────────────────────
  useEffect(() => {
    saveLS("rb_items", items);
    saveLS("rb_lots",  lots);
    saveLS("rb_nextId",    nextId);
    saveLS("rb_nextLotId", nextLotId);
    setSaved(true);
    const t = setTimeout(() => setSaved(false), 1500);
    return () => clearTimeout(t);
  }, [items, lots, nextId, nextLotId]);

  // ─── Stats ───────────────────────────────────────────────────────────────
  const sold  = items.filter(i => i.status === "Vendu");
  const stock = items.filter(i => i.status === "En stock");
  const totalCA       = sold.reduce((s,i) => s + (i.sellPrice||0), 0);
  const totalSoldCost = sold.reduce((s,i) => s + i.buyPrice + i.fees, 0);
  const totalBenef    = totalCA - totalSoldCost;
  const avgMargin     = sold.length ? sold.reduce((s,i) => { const c=i.buyPrice+i.fees; return s+((i.sellPrice-c)/c*100); },0)/sold.length : 0;
  const stockValue    = stock.reduce((s,i) => s + i.buyPrice + i.fees, 0);

  function lotStats(lotId) {
    const li = items.filter(i => i.lotId === lotId);
    const ls = li.filter(i => i.status === "Vendu");
    const lk = li.filter(i => i.status === "En stock");
    const ca       = ls.reduce((s,i) => s+(i.sellPrice||0), 0);
    const cost     = li.reduce((s,i) => s+i.buyPrice+i.fees, 0);
    const soldCost = ls.reduce((s,i) => s+i.buyPrice+i.fees, 0);
    return { total:li.length, sold:ls.length, stock:lk.length, ca, cost, soldCost, benef:ca-soldCost, stockVal:lk.reduce((s,i)=>s+i.buyPrice+i.fees,0) };
  }

  const brandData = (() => {
    const map = {}; sold.forEach(i => { const b=(i.brand||"Autre").trim()||"Autre"; map[b]=(map[b]||0)+1; });
    return Object.entries(map).sort((a,b)=>b[1]-a[1]).map(([label,value],idx)=>({label,value,color:PIE_COLORS[idx%PIE_COLORS.length]}));
  })();
  const brandCAData = (() => {
    const map = {}; sold.forEach(i => { const b=(i.brand||"Autre").trim()||"Autre"; map[b]=(map[b]||0)+(i.sellPrice||0); });
    return Object.entries(map).sort((a,b)=>b[1]-a[1]).map(([label,value],idx)=>({label,value:Math.round(value),color:PIE_COLORS[idx%PIE_COLORS.length]}));
  })();

  const filtered = items.filter(i =>
    (filterStatus==="Tous"||i.status===filterStatus) &&
    (filterCat==="Toutes"||i.category===filterCat) &&
    (filterLot==="Tous"||i.lotId===filterLot||(filterLot==="aucun"&&!i.lotId))
  );

  function addItem() {
    if (!form.name||!form.buyPrice) return;
    const id = nextId; setNextId(id+1);
    setItems(p=>[...p,{id,name:form.name,category:form.category,brand:form.brand||"Autre",buyPrice:parseFloat(form.buyPrice),fees:parseFloat(form.fees)||0,sellPrice:null,platform:form.platform,status:"En stock",date:form.date,sellDate:null,lotId:form.lotId||null}]);
    setForm({name:"",category:"Hauts",brand:"",buyPrice:"",fees:"",platform:"Vinted",date:new Date().toISOString().slice(0,10),lotId:""});
    setAddItemModal(false);
  }

  function confirmSold() {
    if (!sellForm.sellPrice) return;
    setItems(p=>p.map(i=>i.id===sellModal.id?{...i,status:"Vendu",sellPrice:parseFloat(sellForm.sellPrice),sellDate:sellForm.sellDate}:i));
    setSellModal(null);
  }

  function confirmDuplicate() {
    const qty=parseInt(dupForm.quantity)||1;
    const bp=parseFloat(dupForm.buyPrice)||dupModal.buyPrice;
    const fe=parseFloat(dupForm.fees!==""?dupForm.fees:dupModal.fees)||0;
    let id=nextId;
    setItems(p=>[...p,...Array.from({length:qty},()=>({id:id++,name:dupModal.name,category:dupModal.category,brand:dupModal.brand||"Autre",buyPrice:bp,fees:fe,sellPrice:null,platform:dupModal.platform,status:"En stock",date:dupModal.date,sellDate:null,lotId:dupForm.lotId||dupModal.lotId||null}))]);
    setNextId(id);
    setDupModal(null);
  }

  const lotTotal       = lotLines.reduce((s,l)=>s+(parseInt(l.qty)||0)*((parseFloat(l.buyPrice)||0)+(parseFloat(l.fees)||0)),0);
  const lotTotalPieces = lotLines.reduce((s,l)=>s+(parseInt(l.qty)||0),0);

  function confirmCreateLot() {
    if (!lotForm.name) return;
    const lotId=`lot-${nextLotId}`; setNextLotId(nextLotId+1);
    setLots(p=>[...p,{id:lotId,name:lotForm.name,date:lotForm.date,color:lotForm.color}]);
    let id=nextId;
    const newItems=[];
    lotLines.forEach(line=>{
      if(!line.name||!line.buyPrice) return;
      const qty=parseInt(line.qty)||1;
      for(let i=0;i<qty;i++) newItems.push({id:id++,name:line.name,category:line.category,brand:line.brand||"Autre",buyPrice:parseFloat(line.buyPrice)||0,fees:parseFloat(line.fees)||0,sellPrice:null,platform:lotForm.platform,status:"En stock",date:lotForm.date,sellDate:null,lotId});
    });
    setNextId(id);
    setItems(p=>[...p,...newItems]);
    setLotModal(false); setLotForm({name:"",date:new Date().toISOString().slice(0,10),color:LOT_COLORS[0],platform:"Vinted"}); setLotLines([newLine()]);
    setTab("commandes");
  }

  function resetData() {
    if (!window.confirm("Supprimer toutes les données ? Cette action est irréversible.")) return;
    setItems([]); setLots([]); setNextId(20); setNextLotId(3);
  }

  function getLot(lotId) { return lots.find(l=>l.id===lotId); }

  const th=(cols)=>(<thead><tr style={{background:D.card2}}>{cols.map(h=><th key={h} style={{padding:"10px 14px",textAlign:"left",fontWeight:700,color:D.muted,fontSize:"11px",letterSpacing:"0.07em",textTransform:"uppercase",whiteSpace:"nowrap"}}>{h}</th>)}</tr></thead>);
  const sel={...inp,width:"auto",marginTop:0};

  return (
    <div style={{ minHeight:"100vh", background:D.bg, fontFamily:"'DM Sans','Segoe UI',sans-serif", color:D.text }}>

      {/* Header */}
      <div style={{ background:D.card, borderBottom:`1px solid ${D.border}`, padding:"0 24px" }}>
        <div style={{ maxWidth:1100, margin:"0 auto", display:"flex", alignItems:"center", gap:24, height:60 }}>
          <span style={{ fontSize:"18px", color:D.accent, fontWeight:800, whiteSpace:"nowrap" }}>👗 ResellBook</span>
          <nav style={{ display:"flex", gap:2, flex:1 }}>
            {["dashboard","inventaire","commandes","comptabilite"].map(t=>(
              <button key={t} onClick={()=>{setTab(t);setSelectedLot(null);}} style={{background:tab===t?D.accent+"22":"transparent",color:tab===t?D.accent:D.muted,border:tab===t?`1px solid ${D.accent}44`:"1px solid transparent",borderRadius:"8px",padding:"6px 14px",fontSize:"13px",fontWeight:700,cursor:"pointer",textTransform:"capitalize",transition:"all 0.15s"}}>
                {t.charAt(0).toUpperCase()+t.slice(1)}
              </button>
            ))}
          </nav>
          <div style={{ display:"flex", gap:8, alignItems:"center" }}>
            {/* Indicateur sauvegarde */}
            <span style={{ fontSize:"11px", color: saved ? "#4ecf8a" : D.muted, transition:"color 0.3s", whiteSpace:"nowrap" }}>
              {saved ? "✓ Sauvegardé" : "💾 Auto-save"}
            </span>
            <button onClick={()=>exportCSV(items,lots)} style={{ background:D.card2, color:D.text, border:`1px solid ${D.border}`, borderRadius:"8px", padding:"6px 12px", fontSize:"12px", fontWeight:700, cursor:"pointer", whiteSpace:"nowrap" }}>⬇ CSV</button>
            <button onClick={()=>setAddItemModal(true)} style={{ background:D.accent, color:"#fff", border:"none", borderRadius:"10px", padding:"8px 16px", fontSize:"13px", fontWeight:700, cursor:"pointer", whiteSpace:"nowrap" }}>+ Article</button>
          </div>
        </div>
      </div>

      <div style={{ maxWidth:1100, margin:"0 auto", padding:"26px 24px" }}>

        {/* ═══ DASHBOARD ═══ */}
        {tab==="dashboard" && (
          <div>
            <h2 style={{fontSize:"22px",fontWeight:800,marginBottom:18}}>Vue d'ensemble</h2>
            <div style={{display:"grid",gridTemplateColumns:"repeat(auto-fit,minmax(170px,1fr))",gap:12,marginBottom:24}}>
              <StatCard label="Chiffre d'affaires" value={formatEur(totalCA)} sub={`${sold.length} ventes`} accent={D.accent} />
              <StatCard label="Bénéfice net" value={formatEur(totalBenef)} sub="après frais" accent="#4ecf8a" />
              <StatCard label="Marge moyenne" value={`${avgMargin.toFixed(1)}%`} sub="par article" accent="#e0a84a" />
              <StatCard label="Stock" value={formatEur(stockValue)} sub={`${stock.length} articles`} accent="#b07de0" />
            </div>

            {/* Graphique CA */}
            <div style={{background:D.card,borderRadius:"16px",padding:"20px 22px",border:`1px solid ${D.border}`,marginBottom:20}}>
              <div style={{fontSize:"14px",fontWeight:700,marginBottom:16}}>📈 Évolution CA & Bénéfice</div>
              <LineChart items={items} />
            </div>

            <div style={{display:"grid",gridTemplateColumns:"repeat(auto-fit,minmax(300px,1fr))",gap:16,marginBottom:24}}>
              <div style={{background:D.card,borderRadius:"16px",padding:"20px 22px",border:`1px solid ${D.border}`}}>
                <div style={{fontSize:"14px",fontWeight:700,marginBottom:14}}>🥧 Ventes par marque</div>
                <PieChart data={brandData} />
              </div>
              <div style={{background:D.card,borderRadius:"16px",padding:"20px 22px",border:`1px solid ${D.border}`}}>
                <div style={{fontSize:"14px",fontWeight:700,marginBottom:14}}>💶 CA par marque</div>
                <PieChart data={brandCAData} />
              </div>
            </div>

            <h3 style={{fontSize:"15px",fontWeight:700,marginBottom:12}}>Dernières ventes</h3>
            <div style={{background:D.card,borderRadius:"14px",overflow:"hidden",border:`1px solid ${D.border}`,marginBottom:22}}>
              {sold.slice(-5).reverse().map((item,idx)=>{
                const profit=item.sellPrice-item.buyPrice-item.fees; const lot=getLot(item.lotId);
                return (<div key={item.id} style={{display:"flex",alignItems:"center",gap:14,padding:"12px 18px",borderBottom:idx<4?`1px solid ${D.border}`:"none"}}>
                  <span style={{fontSize:"20px"}}>{EMOJI[item.category]}</span>
                  <div style={{flex:1}}><div style={{fontWeight:700,fontSize:"14px"}}>{item.name}</div><div style={{fontSize:"11px",color:D.muted,display:"flex",gap:8,alignItems:"center",marginTop:2}}>{item.brand&&<span style={{color:D.accent}}>{item.brand}</span>}<span>{item.platform} · {item.sellDate}</span>{lot&&<span style={{background:lot.color+"22",color:lot.color,borderRadius:"5px",padding:"1px 7px",fontWeight:700,fontSize:"10px"}}>{lot.name}</span>}</div></div>
                  <div style={{textAlign:"right"}}><div style={{fontWeight:800,fontSize:"15px"}}>{formatEur(item.sellPrice)}</div><div style={{fontSize:"12px",fontWeight:700,color:profit>=0?"#4ecf8a":"#e07878"}}>{profit>=0?"+":""}{formatEur(profit)}</div></div>
                </div>);
              })}
              {sold.length===0&&<div style={{padding:32,textAlign:"center",color:D.muted}}>Aucune vente pour l'instant</div>}
            </div>

            <h3 style={{fontSize:"15px",fontWeight:700,marginBottom:12}}>Résumé des commandes</h3>
            <div style={{display:"grid",gridTemplateColumns:"repeat(auto-fill,minmax(230px,1fr))",gap:12}}>
              {lots.map(lot=>{const s=lotStats(lot.id);return(
                <div key={lot.id} onClick={()=>{setTab("commandes");setSelectedLot(lot.id);}} style={{background:D.card,borderRadius:"14px",padding:"14px 16px",border:`1px solid ${D.border}`,borderTop:`3px solid ${lot.color}`,cursor:"pointer"}}>
                  <div style={{fontWeight:800,fontSize:"14px",marginBottom:3}}>{lot.name}</div>
                  <div style={{fontSize:"11px",color:D.muted,marginBottom:10}}>{lot.date} · {s.total} articles</div>
                  <div style={{display:"flex",justifyContent:"space-between",fontSize:"13px",marginBottom:10}}>
                    <div><div style={{color:D.muted,fontSize:"10px",fontWeight:600}}>CA</div><div style={{fontWeight:700}}>{formatEur(s.ca)}</div></div>
                    <div><div style={{color:D.muted,fontSize:"10px",fontWeight:600}}>BÉNÉFICE</div><div style={{fontWeight:800,color:s.benef>0?"#4ecf8a":s.ca>=s.cost?D.accent:"#e07878"}}>{s.benef>0?"+":""}{formatEur(s.benef)}</div></div>
                    <div><div style={{color:D.muted,fontSize:"10px",fontWeight:600}}>STOCK</div><div style={{fontWeight:700}}>{s.stock} art.</div></div>
                  </div>
                  <LotStatusBadge ca={s.ca} cost={s.cost} benef={s.benef} />
                </div>
              );})}
            </div>
          </div>
        )}

        {/* ═══ INVENTAIRE ═══ */}
        {tab==="inventaire"&&(
          <div>
            <div style={{display:"flex",alignItems:"center",justifyContent:"space-between",marginBottom:16,flexWrap:"wrap",gap:10}}>
              <h2 style={{fontSize:"22px",fontWeight:800,margin:0}}>Inventaire</h2>
              <div style={{display:"flex",gap:8,flexWrap:"wrap"}}>
                <select value={filterStatus} onChange={e=>setFilterStatus(e.target.value)} style={sel}><option>Tous</option><option>En stock</option><option>Vendu</option></select>
                <select value={filterCat} onChange={e=>setFilterCat(e.target.value)} style={sel}><option>Toutes</option>{CATEGORIES.map(c=><option key={c}>{c}</option>)}</select>
                <select value={filterLot} onChange={e=>setFilterLot(e.target.value)} style={sel}><option value="Tous">Toutes commandes</option>{lots.map(l=><option key={l.id} value={l.id}>{l.name}</option>)}<option value="aucun">Sans commande</option></select>
              </div>
            </div>
            <div style={{background:D.card,borderRadius:"14px",overflow:"auto",border:`1px solid ${D.border}`}}>
              <table style={{width:"100%",borderCollapse:"collapse",fontSize:"13px",minWidth:700}}>
                {th(["Article","Marque","Commande","Coût","Prix vente","Bénéfice","Statut","Actions"])}
                <tbody>
                  {filtered.map((item,idx)=>{
                    const cost=item.buyPrice+item.fees; const profit=item.sellPrice!==null?item.sellPrice-cost:null; const lot=getLot(item.lotId);
                    return(<tr key={item.id} style={{borderBottom:`1px solid ${D.border}`,background:idx%2===0?"transparent":D.card2+"88"}}>
                      <td style={{padding:"11px 14px",fontWeight:700}}><div>{EMOJI[item.category]} {item.name}</div><div style={{fontSize:"11px",color:D.muted,fontWeight:400}}>{item.platform} · {item.date}</div></td>
                      <td style={{padding:"11px 14px",color:D.accent,fontWeight:600}}>{item.brand||"—"}</td>
                      <td style={{padding:"11px 14px"}}>{lot?<span style={{background:lot.color+"22",color:lot.color,borderRadius:"6px",padding:"2px 8px",fontWeight:700,fontSize:"11px",whiteSpace:"nowrap"}}>{lot.name}</span>:<span style={{color:D.muted}}>—</span>}</td>
                      <td style={{padding:"11px 14px",fontWeight:600}}>{formatEur(cost)}</td>
                      <td style={{padding:"11px 14px",fontWeight:600}}>{item.sellPrice!==null?formatEur(item.sellPrice):<span style={{color:D.muted}}>—</span>}</td>
                      <td style={{padding:"11px 14px",fontWeight:700,color:profit===null?D.muted:profit>=0?"#4ecf8a":"#e07878"}}>{profit===null?"—":(profit>=0?"+":"")+formatEur(profit)}</td>
                      <td style={{padding:"11px 14px"}}><Badge status={item.status}/></td>
                      <td style={{padding:"11px 14px"}}>
                        <div style={{display:"flex",gap:5}}>
                          {item.status==="En stock"&&<button onClick={()=>{setSellModal(item);setSellForm({sellPrice:"",sellDate:new Date().toISOString().slice(0,10)});}} style={{background:"#4ecf8a22",color:"#4ecf8a",border:"1px solid #4ecf8a44",borderRadius:"7px",padding:"4px 9px",fontSize:"11px",fontWeight:700,cursor:"pointer"}}>✓</button>}
                          <button onClick={()=>{setDupModal(item);setDupForm({quantity:"2",buyPrice:String(item.buyPrice),fees:String(item.fees),lotId:item.lotId||""});}} style={{background:D.accent+"22",color:D.accent,border:`1px solid ${D.accent}44`,borderRadius:"7px",padding:"4px 9px",fontSize:"11px",fontWeight:700,cursor:"pointer"}}>⧉</button>
                          <button onClick={()=>setItems(p=>p.filter(i=>i.id!==item.id))} style={{background:"#e0787822",color:"#e07878",border:"1px solid #e0787844",borderRadius:"7px",padding:"4px 9px",fontSize:"11px",fontWeight:700,cursor:"pointer"}}>✕</button>
                        </div>
                      </td>
                    </tr>);
                  })}
                  {filtered.length===0&&<tr><td colSpan={8} style={{textAlign:"center",padding:40,color:D.muted}}>Aucun article trouvé</td></tr>}
                </tbody>
              </table>
            </div>
          </div>
        )}

        {/* ═══ COMMANDES ═══ */}
        {tab==="commandes"&&!selectedLot&&(
          <div>
            <div style={{display:"flex",alignItems:"center",justifyContent:"space-between",marginBottom:20}}>
              <h2 style={{fontSize:"22px",fontWeight:800,margin:0}}>Commandes groupées</h2>
              <button onClick={()=>setLotModal(true)} style={{background:D.accent,color:"#fff",border:"none",borderRadius:"10px",padding:"8px 16px",fontSize:"13px",fontWeight:700,cursor:"pointer"}}>+ Nouvelle commande</button>
            </div>
            <div style={{display:"grid",gridTemplateColumns:"repeat(auto-fill,minmax(280px,1fr))",gap:16}}>
              {lots.map(lot=>{const s=lotStats(lot.id);return(
                <div key={lot.id} style={{background:D.card,borderRadius:"18px",overflow:"hidden",border:`1px solid ${D.border}`}}>
                  <div style={{background:lot.color+"18",borderBottom:`2px solid ${lot.color}`,padding:"14px 18px"}}>
                    <div style={{display:"flex",alignItems:"center",justifyContent:"space-between"}}>
                      <div style={{fontWeight:800,fontSize:"15px",color:lot.color}}>{lot.name}</div>
                      <LotStatusBadge ca={s.ca} cost={s.cost} benef={s.benef}/>
                    </div>
                    <div style={{fontSize:"12px",color:D.muted,marginTop:4}}>{lot.date} · {s.total} articles au total</div>
                  </div>
                  <div style={{padding:"16px 18px"}}>
                    <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:10,marginBottom:14}}>
                      <div style={{background:D.card2,borderRadius:"10px",padding:"10px 12px"}}><div style={{fontSize:"10px",color:D.muted,fontWeight:600,marginBottom:2}}>INVESTI</div><div style={{fontWeight:800,color:D.text,fontSize:"15px"}}>{formatEur(s.cost)}</div></div>
                      <div style={{background:D.card2,borderRadius:"10px",padding:"10px 12px"}}><div style={{fontSize:"10px",color:D.muted,fontWeight:600,marginBottom:2}}>CA RÉALISÉ</div><div style={{fontWeight:800,color:D.text,fontSize:"15px"}}>{formatEur(s.ca)}</div></div>
                      <div style={{background:s.benef>0?"#4ecf8a18":s.ca>=s.cost?D.accent+"15":"#e0787818",borderRadius:"10px",padding:"10px 12px",border:`1px solid ${s.benef>0?"#4ecf8a33":s.ca>=s.cost?D.accent+"33":"#e0787833"}`}}>
                        <div style={{fontSize:"10px",color:D.muted,fontWeight:600,marginBottom:2}}>BÉNÉFICE</div>
                        <div style={{fontWeight:800,color:s.benef>0?"#4ecf8a":s.ca>=s.cost?D.accent:"#e07878",fontSize:"15px"}}>{s.benef>0?"+":""}{formatEur(s.benef)}</div>
                      </div>
                      <div style={{background:s.stock===0?"#4ecf8a18":"#e0a84a18",borderRadius:"10px",padding:"10px 12px",border:`1px solid ${s.stock===0?"#4ecf8a33":"#e0a84a33"}`}}>
                        <div style={{fontSize:"10px",color:D.muted,fontWeight:600,marginBottom:2}}>STOCK RESTANT</div>
                        <div style={{fontWeight:800,color:s.stock===0?"#4ecf8a":"#e0a84a",fontSize:"15px"}}>{s.stock===0?"✓ Tout vendu":`${s.stock} / ${s.total}`}</div>
                        {s.stock>0&&<div style={{fontSize:"10px",color:D.muted,marginTop:2}}>{formatEur(s.stockVal)} immobilisé</div>}
                      </div>
                    </div>
                    <div style={{marginBottom:s.cost>0&&s.benef<=0?10:14}}>
                      <div style={{display:"flex",justifyContent:"space-between",fontSize:"11px",color:D.muted,marginBottom:5}}><span>Progression des ventes</span><span style={{fontWeight:700,color:lot.color}}>{s.total>0?Math.round((s.sold/s.total)*100):0}%</span></div>
                      <div style={{background:D.card2,borderRadius:"999px",height:8,overflow:"hidden"}}><div style={{background:lot.color,height:"100%",width:s.total>0?`${(s.sold/s.total)*100}%`:"0%",borderRadius:"999px",transition:"width 0.4s ease"}}/></div>
                      <div style={{display:"flex",justifyContent:"space-between",fontSize:"10px",color:D.muted,marginTop:4}}><span>{s.sold} vendu{s.sold>1?"s":""}</span><span>{s.stock} restant{s.stock>1?"s":""}</span></div>
                    </div>
                    {s.cost>0&&s.benef<=0&&(
                      <div style={{marginBottom:14}}>
                        <div style={{display:"flex",justifyContent:"space-between",fontSize:"11px",color:D.muted,marginBottom:5}}><span>Remboursement de la mise</span><span style={{fontWeight:700,color:D.accent}}>{Math.min(100,Math.round((s.ca/s.cost)*100))}%</span></div>
                        <div style={{background:D.card2,borderRadius:"999px",height:6,overflow:"hidden"}}><div style={{background:D.accent,height:"100%",width:`${Math.min(100,(s.ca/s.cost)*100)}%`,borderRadius:"999px",transition:"width 0.4s ease"}}/></div>
                        <div style={{fontSize:"10px",color:D.muted,marginTop:4}}>{formatEur(s.ca)} récupéré sur {formatEur(s.cost)}</div>
                      </div>
                    )}
                    <button onClick={()=>setSelectedLot(lot.id)} style={{width:"100%",background:D.accent,color:"#fff",border:"none",borderRadius:"10px",padding:"9px",fontSize:"13px",fontWeight:700,cursor:"pointer"}}>Voir les articles →</button>
                  </div>
                </div>
              );})}
              {lots.length===0&&<div style={{gridColumn:"1/-1",textAlign:"center",padding:48,color:D.muted}}><div style={{fontSize:36,marginBottom:10}}>📦</div><div style={{fontWeight:700}}>Aucune commande</div></div>}
            </div>
          </div>
        )}

        {/* ═══ DETAIL LOT ═══ */}
        {tab==="commandes"&&selectedLot&&(()=>{
          const lot=getLot(selectedLot); if(!lot) return null;
          const s=lotStats(lot.id); const lotItems=items.filter(i=>i.lotId===lot.id);
          return(<div>
            <button onClick={()=>setSelectedLot(null)} style={{background:"transparent",border:"none",color:D.muted,cursor:"pointer",fontWeight:700,fontSize:"13px",marginBottom:14,padding:0}}>← Retour</button>
            <div style={{display:"flex",alignItems:"center",gap:12,marginBottom:18,flexWrap:"wrap"}}>
              <div style={{width:12,height:12,borderRadius:"50%",background:lot.color}}/>
              <h2 style={{fontSize:"22px",fontWeight:800,margin:0,color:lot.color}}>{lot.name}</h2>
              <span style={{fontSize:"13px",color:D.muted}}>{lot.date}</span>
              <LotStatusBadge ca={s.ca} cost={s.cost} benef={s.benef}/>
            </div>
            <div style={{display:"grid",gridTemplateColumns:"repeat(auto-fit,minmax(150px,1fr))",gap:12,marginBottom:20}}>
              <StatCard label="Investi" value={formatEur(s.cost)} sub={`${s.total} articles`} accent={lot.color}/>
              <StatCard label="CA réalisé" value={formatEur(s.ca)} sub={`${s.sold} vendus`} accent={D.accent}/>
              <StatCard label="Bénéfice" value={(s.benef>0?"+":"")+formatEur(s.benef)} sub="sur ventes" accent={s.benef>0?"#4ecf8a":s.ca>=s.cost?D.accent:"#e07878"}/>
              <StatCard label="Stock restant" value={s.stock===0?"✓ Tout vendu":`${s.stock} / ${s.total}`} sub={s.stock>0?formatEur(s.stockVal)+" immobilisé":"Félicitations !"} accent={s.stock===0?"#4ecf8a":"#e0a84a"}/>
            </div>
            <div style={{background:D.card,borderRadius:"14px",overflow:"auto",border:`1px solid ${D.border}`}}>
              <table style={{width:"100%",borderCollapse:"collapse",fontSize:"13px",minWidth:520}}>
                {th(["Article","Marque","Coût","Prix vente","Bénéfice","Statut","Actions"])}
                <tbody>
                  {lotItems.map((item,idx)=>{
                    const cost=item.buyPrice+item.fees; const profit=item.sellPrice!==null?item.sellPrice-cost:null;
                    return(<tr key={item.id} style={{borderBottom:`1px solid ${D.border}`,background:idx%2===0?"transparent":D.card2+"88"}}>
                      <td style={{padding:"11px 14px",fontWeight:700}}>{EMOJI[item.category]} {item.name}</td>
                      <td style={{padding:"11px 14px",color:D.accent,fontWeight:600}}>{item.brand||"—"}</td>
                      <td style={{padding:"11px 14px"}}>{formatEur(cost)}</td>
                      <td style={{padding:"11px 14px",fontWeight:600}}>{item.sellPrice!==null?formatEur(item.sellPrice):<span style={{color:D.muted}}>—</span>}</td>
                      <td style={{padding:"11px 14px",fontWeight:700,color:profit===null?D.muted:profit>=0?"#4ecf8a":"#e07878"}}>{profit===null?"—":(profit>=0?"+":"")+formatEur(profit)}</td>
                      <td style={{padding:"11px 14px"}}><Badge status={item.status}/></td>
                      <td style={{padding:"11px 14px"}}>
                        <div style={{display:"flex",gap:6}}>
                          {item.status==="En stock"&&<button onClick={()=>{setSellModal(item);setSellForm({sellPrice:"",sellDate:new Date().toISOString().slice(0,10)});}} style={{background:"#4ecf8a22",color:"#4ecf8a",border:"1px solid #4ecf8a44",borderRadius:"7px",padding:"4px 9px",fontSize:"11px",fontWeight:700,cursor:"pointer"}}>✓ Vendu</button>}
                          <button onClick={()=>{setDupModal(item);setDupForm({quantity:"2",buyPrice:String(item.buyPrice),fees:String(item.fees),lotId:item.lotId||""});}} style={{background:D.accent+"22",color:D.accent,border:`1px solid ${D.accent}44`,borderRadius:"7px",padding:"4px 9px",fontSize:"11px",fontWeight:700,cursor:"pointer"}}>⧉</button>
                        </div>
                      </td>
                    </tr>);
                  })}
                  {lotItems.length===0&&<tr><td colSpan={7} style={{textAlign:"center",padding:32,color:D.muted}}>Aucun article</td></tr>}
                </tbody>
              </table>
            </div>
          </div>);
        })()}

        {/* ═══ COMPTABILITE ═══ */}
        {tab==="comptabilite"&&(
          <div>
            <div style={{display:"flex",alignItems:"center",justifyContent:"space-between",marginBottom:20,flexWrap:"wrap",gap:10}}>
              <h2 style={{fontSize:"22px",fontWeight:800,margin:0}}>Comptabilité</h2>
              <div style={{display:"flex",gap:8}}>
                <button onClick={()=>exportCSV(items,lots)} style={{background:D.card2,color:D.text,border:`1px solid ${D.border}`,borderRadius:"8px",padding:"8px 14px",fontSize:"13px",fontWeight:700,cursor:"pointer"}}>⬇ Exporter CSV</button>
                <button onClick={resetData} style={{background:"#e0787815",color:"#e07878",border:"1px solid #e0787833",borderRadius:"8px",padding:"8px 14px",fontSize:"13px",fontWeight:700,cursor:"pointer"}}>🗑 Réinitialiser</button>
              </div>
            </div>
            <div style={{display:"grid",gridTemplateColumns:"repeat(auto-fit,minmax(185px,1fr))",gap:12,marginBottom:26}}>
              <StatCard label="Total investi" value={formatEur(items.reduce((s,i)=>s+i.buyPrice+i.fees,0))} sub="tous achats" accent="#e0a84a"/>
              <StatCard label="Chiffre d'affaires" value={formatEur(totalCA)} sub={`${sold.length} ventes`} accent={D.accent}/>
              <StatCard label="Bénéfice net" value={formatEur(totalBenef)} sub="CA - coûts vendus" accent="#4ecf8a"/>
              <StatCard label="ROI global" value={totalSoldCost>0?`${((totalBenef/totalSoldCost)*100).toFixed(1)}%`:"—"} sub="retour sur invest." accent="#b07de0"/>
            </div>
            <h3 style={{fontSize:"15px",fontWeight:700,marginBottom:12}}>Bilan par commande</h3>
            <div style={{background:D.card,borderRadius:"14px",overflow:"auto",border:`1px solid ${D.border}`,marginBottom:24}}>
              <table style={{width:"100%",borderCollapse:"collapse",fontSize:"13px",minWidth:680}}>
                {th(["Commande","Articles","Investi","CA réalisé","Bénéfice","Stock restant","Bilan"])}
                <tbody>
                  {lots.map((lot,idx)=>{const s=lotStats(lot.id);return(
                    <tr key={lot.id} style={{borderBottom:`1px solid ${D.border}`,background:idx%2===0?"transparent":D.card2+"88"}}>
                      <td style={{padding:"11px 14px"}}><div style={{display:"flex",alignItems:"center",gap:8}}><div style={{width:8,height:8,borderRadius:"50%",background:lot.color}}/><span style={{fontWeight:700}}>{lot.name}</span></div><div style={{fontSize:"11px",color:D.muted,paddingLeft:16}}>{lot.date}</div></td>
                      <td style={{padding:"11px 14px"}}>{s.total}</td>
                      <td style={{padding:"11px 14px",fontWeight:600}}>{formatEur(s.cost)}</td>
                      <td style={{padding:"11px 14px",fontWeight:600}}>{formatEur(s.ca)}</td>
                      <td style={{padding:"11px 14px",fontWeight:800,color:s.benef>0?"#4ecf8a":s.ca>=s.cost?D.accent:"#e07878"}}>{s.benef>0?"+":""}{formatEur(s.benef)}</td>
                      <td style={{padding:"11px 14px"}}>{s.stock===0?<span style={{color:"#4ecf8a",fontWeight:700}}>✓ Tout vendu</span>:<span style={{color:"#e0a84a",fontWeight:700}}>{s.stock} art. · {formatEur(s.stockVal)}</span>}</td>
                      <td style={{padding:"11px 14px"}}><LotStatusBadge ca={s.ca} cost={s.cost} benef={s.benef}/></td>
                    </tr>
                  );})}
                  {lots.length>0&&(<tr style={{background:D.accent+"11",borderTop:`2px solid ${D.accent}44`}}>
                    <td colSpan={2} style={{padding:"12px 14px",color:D.accent,fontWeight:800}}>TOTAL</td>
                    <td style={{padding:"12px 14px",fontWeight:800}}>{formatEur(items.reduce((s,i)=>s+i.buyPrice+i.fees,0))}</td>
                    <td style={{padding:"12px 14px",fontWeight:800}}>{formatEur(totalCA)}</td>
                    <td style={{padding:"12px 14px",color:"#4ecf8a",fontWeight:800}}>+{formatEur(totalBenef)}</td>
                    <td style={{padding:"12px 14px",fontWeight:800}}>{formatEur(stockValue)}</td>
                    <td/>
                  </tr>)}
                </tbody>
              </table>
            </div>
            <h3 style={{fontSize:"15px",fontWeight:700,marginBottom:12}}>Détail des ventes</h3>
            <div style={{background:D.card,borderRadius:"14px",overflow:"auto",border:`1px solid ${D.border}`}}>
              <table style={{width:"100%",borderCollapse:"collapse",fontSize:"13px",minWidth:660}}>
                {th(["Article","Marque","Commande","Date vente","Coût","Prix vente","Bénéfice","Marge %"])}
                <tbody>
                  {sold.map((item,idx)=>{
                    const cost=item.buyPrice+item.fees; const profit=item.sellPrice-cost; const margin=((profit/cost)*100).toFixed(1); const lot=getLot(item.lotId);
                    return(<tr key={item.id} style={{borderBottom:`1px solid ${D.border}`,background:idx%2===0?"transparent":D.card2+"88"}}>
                      <td style={{padding:"11px 14px",fontWeight:700}}>{EMOJI[item.category]} {item.name}</td>
                      <td style={{padding:"11px 14px",color:D.accent,fontWeight:600}}>{item.brand||"—"}</td>
                      <td style={{padding:"11px 14px"}}>{lot?<span style={{background:lot.color+"22",color:lot.color,borderRadius:"6px",padding:"2px 7px",fontWeight:700,fontSize:"11px"}}>{lot.name}</span>:<span style={{color:D.muted}}>—</span>}</td>
                      <td style={{padding:"11px 14px",color:D.muted}}>{item.sellDate}</td>
                      <td style={{padding:"11px 14px"}}>{formatEur(cost)}</td>
                      <td style={{padding:"11px 14px",fontWeight:700}}>{formatEur(item.sellPrice)}</td>
                      <td style={{padding:"11px 14px",fontWeight:800,color:profit>=0?"#4ecf8a":"#e07878"}}>{profit>=0?"+":""}{formatEur(profit)}</td>
                      <td style={{padding:"11px 14px",fontWeight:700,color:parseFloat(margin)>=0?"#4ecf8a":"#e07878"}}>{margin}%</td>
                    </tr>);
                  })}
                  {sold.length===0&&<tr><td colSpan={8} style={{textAlign:"center",padding:40,color:D.muted}}>Aucune vente</td></tr>}
                </tbody>
              </table>
            </div>
          </div>
        )}
      </div>

      {/* ═══ MODAL Créer commande ═══ */}
      <Modal open={lotModal} onClose={()=>setLotModal(false)} wide>
        <h3 style={{fontSize:"18px",color:D.text,margin:"0 0 18px",fontWeight:800}}>🗂️ Nouvelle commande</h3>
        <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:10,marginBottom:16}}>
          <div style={{gridColumn:"1/-1"}}><label style={lbl}>Nom de la commande</label><input style={inp} placeholder="Ex: Lot Levi's hommes · Mars 2026" value={lotForm.name} onChange={e=>setLotForm(f=>({...f,name:e.target.value}))}/></div>
          <div><label style={lbl}>Date</label><input style={inp} type="date" value={lotForm.date} onChange={e=>setLotForm(f=>({...f,date:e.target.value}))}/></div>
          <div><label style={lbl}>Plateforme</label><select style={inp} value={lotForm.platform} onChange={e=>setLotForm(f=>({...f,platform:e.target.value}))}>{PLATFORMS.map(p=><option key={p}>{p}</option>)}</select></div>
          <div style={{gridColumn:"1/-1"}}><label style={lbl}>Couleur</label><div style={{display:"flex",gap:8,marginTop:8}}>{LOT_COLORS.map(c=><button key={c} onClick={()=>setLotForm(f=>({...f,color:c}))} style={{width:26,height:26,borderRadius:"50%",background:c,border:lotForm.color===c?`3px solid ${D.text}`:"3px solid transparent",cursor:"pointer"}}/>)}</div></div>
        </div>
        <div style={{borderTop:`1px solid ${D.border}`,margin:"16px 0"}}/>
        <div style={{display:"flex",alignItems:"center",justifyContent:"space-between",marginBottom:12}}>
          <div style={{fontSize:"14px",fontWeight:700}}>Articles de la commande</div>
          <button onClick={()=>setLotLines(p=>[...p,newLine()])} style={{background:D.accent+"22",color:D.accent,border:`1px solid ${D.accent}44`,borderRadius:"8px",padding:"5px 12px",fontSize:"12px",fontWeight:700,cursor:"pointer"}}>+ Ajouter un article</button>
        </div>
        <div style={{display:"flex",flexDirection:"column",gap:12,marginBottom:16}}>
          {lotLines.map((line,i)=>(<ArticleLine key={line._id} line={line} onChange={u=>setLotLines(p=>p.map((l,j)=>j===i?u:l))} onRemove={()=>setLotLines(p=>p.filter((_,j)=>j!==i))} canRemove={lotLines.length>1}/>))}
        </div>
        {lotTotalPieces>0&&(<div style={{background:D.card2,borderRadius:"12px",padding:"14px 16px",border:`1px solid ${D.border}`,marginBottom:16,display:"flex",justifyContent:"space-between",alignItems:"center"}}>
          <div><div style={{fontSize:"12px",color:D.muted,fontWeight:600}}>TOTAL COMMANDE</div><div style={{fontSize:"13px",color:D.text,marginTop:2}}>{lotTotalPieces} pièce{lotTotalPieces>1?"s":""} · {lotLines.filter(l=>l.name).length} référence{lotLines.filter(l=>l.name).length>1?"s":""}</div></div>
          <div style={{fontSize:"22px",fontWeight:800,color:D.accent}}>{formatEur(lotTotal)}</div>
        </div>)}
        <div style={{display:"flex",gap:10}}>
          <button onClick={()=>{setLotModal(false);setLotLines([newLine()]);}} style={{flex:1,padding:"10px",borderRadius:"10px",background:"transparent",border:`1px solid ${D.border}`,color:D.muted,cursor:"pointer",fontWeight:700}}>Annuler</button>
          <button onClick={confirmCreateLot} style={{flex:2,padding:"10px",borderRadius:"10px",border:"none",background:D.accent,color:"#fff",cursor:"pointer",fontWeight:800}}>Créer la commande {lotTotalPieces>0?`(${lotTotalPieces} articles)`:""}</button>
        </div>
      </Modal>

      {/* ═══ MODAL Article seul ═══ */}
      <Modal open={addItemModal} onClose={()=>setAddItemModal(false)}>
        <h3 style={{fontSize:"18px",color:D.text,margin:"0 0 16px",fontWeight:800}}>Nouvel article</h3>
        <div style={{display:"flex",flexDirection:"column",gap:11}}>
          <div><label style={lbl}>Nom</label><input style={inp} placeholder="Ex: Jean Levi's 501 homme" value={form.name} onChange={e=>setForm(f=>({...f,name:e.target.value}))}/></div>
          <div><label style={lbl}>Marque</label><input style={inp} placeholder="Ex: Levi's, Zara, H&M..." value={form.brand} onChange={e=>setForm(f=>({...f,brand:e.target.value}))}/></div>
          <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:10}}>
            <div><label style={lbl}>Catégorie</label><select style={inp} value={form.category} onChange={e=>setForm(f=>({...f,category:e.target.value}))}>{CATEGORIES.map(c=><option key={c}>{c}</option>)}</select></div>
            <div><label style={lbl}>Plateforme</label><select style={inp} value={form.platform} onChange={e=>setForm(f=>({...f,platform:e.target.value}))}>{PLATFORMS.map(p=><option key={p}>{p}</option>)}</select></div>
          </div>
          <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:10}}>
            <div><label style={lbl}>Prix d'achat (€)</label><input style={inp} type="number" placeholder="0.00" value={form.buyPrice} onChange={e=>setForm(f=>({...f,buyPrice:e.target.value}))}/></div>
            <div><label style={lbl}>Frais (€)</label><input style={inp} type="number" placeholder="0.00" value={form.fees} onChange={e=>setForm(f=>({...f,fees:e.target.value}))}/></div>
          </div>
          <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:10}}>
            <div><label style={lbl}>Date d'achat</label><input style={inp} type="date" value={form.date} onChange={e=>setForm(f=>({...f,date:e.target.value}))}/></div>
            <div><label style={lbl}>Commande</label><select style={inp} value={form.lotId} onChange={e=>setForm(f=>({...f,lotId:e.target.value}))}><option value="">Aucune</option>{lots.map(l=><option key={l.id} value={l.id}>{l.name}</option>)}</select></div>
          </div>
          <div style={{display:"flex",gap:10,marginTop:4}}>
            <button onClick={()=>setAddItemModal(false)} style={{flex:1,padding:"10px",borderRadius:"10px",background:"transparent",border:`1px solid ${D.border}`,color:D.muted,cursor:"pointer",fontWeight:700}}>Annuler</button>
            <button onClick={addItem} style={{flex:2,padding:"10px",borderRadius:"10px",border:"none",background:D.accent,color:"#fff",cursor:"pointer",fontWeight:800}}>Ajouter</button>
          </div>
        </div>
      </Modal>

      {/* ═══ MODAL Dupliquer ═══ */}
      <Modal open={!!dupModal} onClose={()=>setDupModal(null)}>
        <h3 style={{fontSize:"18px",color:D.text,margin:"0 0 4px",fontWeight:800}}>Dupliquer en masse</h3>
        <p style={{color:D.muted,fontSize:"13px",marginBottom:14}}>{EMOJI[dupModal?.category]} {dupModal?.name}</p>
        <div style={{display:"flex",flexDirection:"column",gap:11}}>
          <div><label style={lbl}>Nombre de copies</label><input style={inp} type="number" min="1" max="999" value={dupForm.quantity} onChange={e=>setDupForm(f=>({...f,quantity:e.target.value}))}/>{parseInt(dupForm.quantity)>0&&<div style={{fontSize:"11px",color:D.muted,marginTop:4}}>→ {parseInt(dupForm.quantity)} articles ajoutés</div>}</div>
          <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:10}}>
            <div><label style={lbl}>Prix unitaire (€)</label><input style={inp} type="number" value={dupForm.buyPrice} onChange={e=>setDupForm(f=>({...f,buyPrice:e.target.value}))}/></div>
            <div><label style={lbl}>Frais unitaires (€)</label><input style={inp} type="number" value={dupForm.fees} onChange={e=>setDupForm(f=>({...f,fees:e.target.value}))}/></div>
          </div>
          <div><label style={lbl}>Commande</label><select style={inp} value={dupForm.lotId} onChange={e=>setDupForm(f=>({...f,lotId:e.target.value}))}><option value="">Aucune</option>{lots.map(l=><option key={l.id} value={l.id}>{l.name}</option>)}</select></div>
          {dupForm.quantity&&dupForm.buyPrice&&(<div style={{background:D.card2,borderRadius:"10px",padding:"10px 14px",fontSize:"13px",display:"flex",justifyContent:"space-between",border:`1px solid ${D.border}`}}><span style={{color:D.muted}}>Investissement total</span><span style={{fontWeight:800,color:D.accent}}>{formatEur((parseFloat(dupForm.buyPrice)+parseFloat(dupForm.fees||0))*parseInt(dupForm.quantity))}</span></div>)}
          <div style={{display:"flex",gap:10,marginTop:4}}>
            <button onClick={()=>setDupModal(null)} style={{flex:1,padding:"10px",borderRadius:"10px",background:"transparent",border:`1px solid ${D.border}`,color:D.muted,cursor:"pointer",fontWeight:700}}>Annuler</button>
            <button onClick={confirmDuplicate} style={{flex:2,padding:"10px",borderRadius:"10px",border:"none",background:D.accent,color:"#fff",cursor:"pointer",fontWeight:800}}>⧉ Créer {parseInt(dupForm.quantity)||0} articles</button>
          </div>
        </div>
      </Modal>

      {/* ═══ MODAL Vendu ═══ */}
      <Modal open={!!sellModal} onClose={()=>setSellModal(null)}>
        <h3 style={{fontSize:"18px",color:D.text,margin:"0 0 4px",fontWeight:800}}>Marquer comme vendu</h3>
        <p style={{color:D.muted,fontSize:"13px",marginBottom:14}}>{sellModal?.name}</p>
        <div style={{display:"flex",flexDirection:"column",gap:11}}>
          <div><label style={lbl}>Prix de vente (€)</label><input style={inp} type="number" placeholder="0.00" value={sellForm.sellPrice} onChange={e=>setSellForm(f=>({...f,sellPrice:e.target.value}))}/></div>
          <div><label style={lbl}>Date de vente</label><input style={inp} type="date" value={sellForm.sellDate} onChange={e=>setSellForm(f=>({...f,sellDate:e.target.value}))}/></div>
          {sellModal&&sellForm.sellPrice&&(()=>{const profit=parseFloat(sellForm.sellPrice)-sellModal.buyPrice-sellModal.fees;return(<div style={{background:D.card2,borderRadius:"10px",padding:"10px 14px",fontSize:"13px",border:`1px solid ${D.border}`}}><div style={{display:"flex",justifyContent:"space-between"}}><span style={{color:D.muted}}>Coût</span><span style={{fontWeight:700}}>{formatEur(sellModal.buyPrice+sellModal.fees)}</span></div><div style={{display:"flex",justifyContent:"space-between",marginTop:4}}><span style={{color:D.muted}}>Bénéfice</span><span style={{fontWeight:800,color:profit>=0?"#4ecf8a":"#e07878"}}>{profit>=0?"+":""}{formatEur(profit)}</span></div></div>);})()}
          <div style={{display:"flex",gap:10,marginTop:4}}>
            <button onClick={()=>setSellModal(null)} style={{flex:1,padding:"10px",borderRadius:"10px",background:"transparent",border:`1px solid ${D.border}`,color:D.muted,cursor:"pointer",fontWeight:700}}>Annuler</button>
            <button onClick={confirmSold} style={{flex:2,padding:"10px",borderRadius:"10px",border:"none",background:"#4ecf8a",color:"#0f0f14",cursor:"pointer",fontWeight:800}}>Confirmer ✓</button>
          </div>
        </div>
      </Modal>
    </div>
  );
}
