-- 仲介提交成交時，只能選擇已核准且已刊登建案的未售戶別。
drop policy if exists "units brokers read published projects" on public.units;
create policy "units brokers read published projects"
on public.units for select to authenticated
using (
  exists (
    select 1 from public.projects p
    where p.name = public.units.project_name
      and p.published = true
      and p.approval_status = 'approved'
  )
);
