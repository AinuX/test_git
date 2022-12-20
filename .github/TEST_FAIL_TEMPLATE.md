---
title: "{{ env.TITLE }}"
labels: [bug]
---
The {{ env.WORKFLOW }} workflow failed on {{ date | date("YYYY-MM-DD HH:mm") }} UTC

Full run: https://github.com/{{ env.REPO }}/actions/runs/{{ env.RUN_ID }}

##Pytest HTML report

{{ env.REPORT_URL }}

(This post will be updated if another test fails, as long as this issue remains open.)
