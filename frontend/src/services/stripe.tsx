import { NextApiRequest, NextApiResponse } from 'next';
import Stripe from 'stripe';

const stripe = new Stripe(process.env.STRIPE_SECRET_KEY!);

export default async function handler(req: NextApiRequest, res: NextApiResponse) {
  const { session_id } = req.query;

  if (req.method === 'GET') {
    try {
      if (typeof session_id === 'string') {
        const session = await stripe.checkout.sessions.retrieve(session_id);
        res.status(200).json(session);
      } else {
        res.status(400).json({ error: 'Invalid session ID' });
      }
    } catch (error) {
      res.status(500).json({ error: 'Error retrieving session data' });
    }
  } else {
    res.status(405).json({ error: 'Method not allowed' });
  }
}