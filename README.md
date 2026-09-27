## Calroie Tracker

This is my first project after University, mostly wanted to create an actually free Calorie tracker app to assist my journey in understanding how calorie tracking works, what actually matters and somewhat help me decide what I will eat. So far my experience with these apps has been mixed, it usually starts with them being free and working fantastically. Turns quickly into Paid Subscriptions and so on... It's not great. So this is sort of my contribution that I am working with. I found a website that has a database of Barcodes for most food items called "openfoodfacts". Let's see where it goes from here.

So current plan:
- Access your camera (computer or phone) to scan a barcode
- Talk to the "openfoodfacts" database for calorie information
- Add it to a summary
- Track your goals

Currently actually finished:
- Access to the Database
- Manual insertion of barcode numbers to get nutritional values

## NOTE!

This project has just been started, all the requirements and other information will come with time. 

## Supabase diary setup

1. In the Supabase dashboard, open **SQL Editor**, paste the contents of `supabase/schema.sql`, and run it once.
2. In Supabase **Authentication → Providers → Email**, leave the Email provider enabled (Supabase uses it internally for password auth) and turn **Confirm email** off. The app presents username/password; it maps each username to a non-deliverable internal address because Supabase Auth does not natively support username login. Since that address cannot receive mail, users cannot use email-based password recovery; keep a safe copy of the password.
3. In Vercel → **Project Settings → Environment Variables**, add `SUPABASE_URL` and `SUPABASE_PUBLISHABLE_KEY`. The app also accepts `SUPABASE_KEY` for compatibility, but its value must begin with `sb_publishable_`. Never use a secret or service-role key here; the browser receives this key and row-level security protects diary entries.
4. Redeploy the Vercel project so the environment variables are available.

The web app supports account creation/sign-in, logging the currently displayed product with a serving amount, viewing today's calorie total and entries, and removing entries. Diary access requires a signed-in Supabase user and the row-level security policies in `supabase/schema.sql`.
