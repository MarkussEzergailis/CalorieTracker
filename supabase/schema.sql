-- Run this once in Supabase Dashboard → SQL Editor.
create table public.food_entries (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references auth.users(id) on delete cascade,
  eaten_at timestamptz not null default now(),
  product_name text not null,
  brand text,
  barcode text,
  servings numeric(8, 2) not null default 1 check (servings > 0),
  calories_per_serving_kcal numeric(9, 2),
  protein_per_serving_g numeric(9, 2),
  carbs_per_serving_g numeric(9, 2),
  fat_per_serving_g numeric(9, 2)
);

create index food_entries_user_date_idx
  on public.food_entries (user_id, eaten_at desc);

alter table public.food_entries enable row level security;

create policy "Users can read their own entries"
  on public.food_entries for select to authenticated
  using ((select auth.uid()) = user_id);

create policy "Users can add their own entries"
  on public.food_entries for insert to authenticated
  with check ((select auth.uid()) = user_id);

create policy "Users can delete their own entries"
  on public.food_entries for delete to authenticated
  using ((select auth.uid()) = user_id);

grant select, insert, delete on public.food_entries to authenticated;
