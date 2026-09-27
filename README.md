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
2. In Supabase **Authentication** settings, configure the site URL and allowed redirect URLs for your Vercel site. Email confirmation may be enabled for new accounts.
3. In Vercel → **Project Settings → Environment Variables**, add `SUPABASE_URL` and `SUPABASE_PUBLISHABLE_KEY`. Use a publishable/anon key only. Never use a secret or service-role key here; the browser receives this key and row-level security protects diary entries.
4. Redeploy the Vercel project so the environment variables are available.

The web app supports account creation/sign-in, logging the currently displayed product with a serving amount, viewing today's calorie total and entries, and removing entries. Diary access requires a signed-in Supabase user and the row-level security policies in `supabase/schema.sql`.
