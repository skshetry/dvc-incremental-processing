```console
dvc dag --md --mermaid
```

```mermaid
flowchart TD
	node1["prune"]
	node2["downstream"]
	node3["process@dataset1"]
	node4["process@dataset2"]
	node5["process@dataset3"]
	node3-->node2
	node4-->node2
	node5-->node2
```
