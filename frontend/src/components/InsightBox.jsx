import React from 'react'
export default function InsightBox({insight}){
return (
<div className="p-4 bg-gray-800 rounded">
<h3 className="text-sm opacity-80">AI Insights</h3>
<div className="mt-2 text-sm leading-relaxed">
{insight ? <pre className="whitespace-pre-wrap">{insight}</pre> : <div>No insight yet — ask AI.</div>}
</div>
</div>
)
}
